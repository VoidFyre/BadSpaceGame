import pygame


class SpaceshipView:
    def __init__(self):
        self.image = pygame.image.load("./assets/interface/inventory_screen.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, screen, spaceship):
        screen.blit(self.image, (spaceship.x - self.width/2, spaceship.y - self.height/2))
