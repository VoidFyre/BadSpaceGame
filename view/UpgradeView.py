import pygame
import os

class UpgradeView:
    def __init__(self):
        self.images = {
            'uncommon_orb': pygame.image.load(os.path.join("assets", "upgrade-orb/uncommon_orb.png")),
            'rare_orb': pygame.image.load(os.path.join("assets", "upgrade-orb/rare_orb.png")),
            'epic_orb': pygame.image.load(os.path.join("assets", "upgrade-orb/epic_orb.png")),
            'legendary_orb': pygame.image.load(os.path.join("assets", "upgrade-orb/legendary_orb.png"))
        }
        self.width = 30
        self.height = 30

    def draw(self, window, orb, x, y):
        window.blit(self.images[orb], (x, y))