import sys, pygame, random
from pygame.locals import *
from ship import Ship
from asteroid import Asteroid

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sonidos/viento.mp3")
    pygame.mixer.music.play(1)
    background_image = pygame.image.load("imagenes/space.png")
    background_rect = background_image.get_rect()
    
    pygame.display.set_caption( "asteroids" )
    
    ship = Ship(size)
    
    asteroids = []

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        screen.blit(background_image, background_rect)
        fuente = pygame.font.Font(None, 45)
        texto_puntos = fuente.render("Puntos: " + str(ship.puntos), 1, (250, 250, 250))
        texto_vida = fuente.render("Vida: " + str(ship.vida), 1, (250, 250, 250))
        fuente_go = pygame.font.Font(None, 100)
        texto_fin = fuente_go.render("FIN DEL JUEGO", 1, (250, 0, 0))
        
        ship.update()
        
        for bullet in ship.bullets:
            bullet.update()
            if bullet.alcance == 0:
                ship.bullets.remove(bullet)
            screen.blit(bullet.image, bullet.rect) 
        screen.blit(ship.image, ship.rect)

        for asteroid in asteroids:
            asteroids.update()
            screen.blit(asteroid.image, asteroid.rect)
            for bullet in ship.bullets:
                if asteroid.rect.colliderect(bullet.rect):
                    ship.bullets.remove(bullet)
                    ship.puntos += 1
                    if asteroid in asteroids:
                        asteroid.explotar()
                        screen.blit(asteroid.image, asteroid.rect)
                        asteroids.remove(asteroid)

        if ship.vida > 0:
            screen.blit(texto_vida, (600, 50))
            screen.blit(texto_puntos, (100, 50))
        else:
            screen.blit(texto_fin, (150, 250))
        
        pygame.display.update()
        pygame.time.delay(10)
            
if __name__ == '__main__': 
    main()
