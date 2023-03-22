import pygame

class EnemyView:
    def __init__(self):
        self.image = pygame.image.load("./assets/interface/inventory_screen.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, screen, enemy):
        screen.blit(self.image, (enemy.x - self.width/2, enemy.y - self.height/2))
