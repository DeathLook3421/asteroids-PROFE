import pygame, math
from pygame.sprite import Sprite
from pygame.locals import *
from bullet import Bullet

class Ship(Sprite):
    def __init__(self, contenedor):
        Sprite.__init__(self)
        self.angulo = 0
        self.radio = 8
        self.puntos = 0
        self.vida = 100
        self.vel = [0,0]
        self.bullets = []
        self.carga = True
        self.contenedor = contenedor
        self.base_image = pygame.image.load("imagenes/ship.png")
        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.rect.move_ip(contenedor[0]/2, contenedor[1]/2)
        self.impulso = pygame.mixer.Sound('sonidos/impulso.wav')
        self.impulso.set_volume(0.05)
        self.disparo = pygame.mixer.Sound('sonidos/disparo.wav')
        self.disparo.set_volume(0.05)
        
        
    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.rotar(2)
        elif teclas[K_RIGHT]:
            self.rotar(-2)
        elif teclas[K_UP]:
            self.acelerar()
        elif teclas[K_SPACE]:
            self.disparar()
          
        self.vel[0] *= 0.99
        self.vel[1] *= 0.99
        self.rect = self.rect.move(self.vel)
        self.rect.x = self.rect.x % self.contenedor[0]
        self.rect.y = self.rect.y % self.contenedor[1]
    
    def disparar(self):
        self.disparo.play()
        vector = [0,0]
        vector[0] += math.cos(math.radians((self.angulo)%360))
        vector[1] -= math.sin(math.radians((self.angulo)%360))
        pos = [self.rect.x + self.radio, self.rect.y + self.radio]
        vel = [self.vel[0] + 6 * vector[0], self.vel[1] + 6 * vector[1]]
        self.bullets.append(Bullet(pos,self.angulo, vel, self.contenedor))
    
    def acelerar(self):
        self.impulso.play()
        self.vel[0] += math.cos(math.radians((self.angulo)%360))
        self.vel[1] -= math.sin(math.radians((self.angulo)%360))

    def rotar(self, angulo):
        self.angulo += angulo
        centerx = self.rect.centerx
        centery = self.rect.centery
        self.image = pygame.transform.rotate(self.base_image, self.angulo)
        self.rect = self.image.get_rect() 
        self.rect.centerx = centerx
        self.rect.centery = centery
