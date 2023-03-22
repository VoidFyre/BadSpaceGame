import pygame

class PowerUpView:
    def __init__(self):
        self.images = {
            'weapon': pygame.image.load("./assets/interface/inventory_screen.png"),
            'shield': pygame.image.load("./assets/interface/inventory_screen.png"),
            'speed': pygame.image.load("./assets/interface/inventory_screen.png")
        }
        self.width = self.images['weapon'].get_width()
        self.height = self.images['weapon'].get_height()

    def draw(self, screen, powerup):
        image = self.images[powerup.type]
        screen.blit(image, (powerup.x - self.width/2, powerup.y - self.height/2))