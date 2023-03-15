import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, equipped, inventory, posx, posy):
        super().__init__()

        self.posx = posx
        self.posy = posy
        self.base_health = 300
        self.base_armor = 100
        self.base_shield = 100
        self.equipped = {'primary': None, 'secondary': None, 'hull': None, 'armor': None, 'shield': None, 'thruster': None}
        self.inventory = [None, None, None, None, None, None]

        self.image = pygame.image.load("./assets/ship_base.png")

    def shootPrimary(self):
        color = {0,0,0}
        self.primary = self.equipped['primary']
        #self.projectile = #projectile image

        self.projectileVel = {0,1}

        projectile = pygame.draw.rect(self.primary.image, color, pygame.Rect(self.posx, self.posy, self.primary.x, self.primary.y))

        projectile.colliderect()



