import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, speed, damage, homing, ability, image):
        super().__init__()
        self.speed = speed
        self.damage = damage
        self.homing = homing
        self.ability = ability
        self.image = image