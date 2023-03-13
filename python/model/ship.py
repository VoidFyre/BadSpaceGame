import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, equipped, inventory, posx, posy):
        super().__init__()

        self.base_health = 300
        self.base_armor = 100
        self.base_shield = 100
        self.equipped = {'primary': None, 'secondary': None, 'hull': None, 'armor': None, 'shield': None, 'thruster': None}
        self.inventory = [None, None, None, None, None, None]

        self.image = pygame.image.load("./assets/ship_base.png")