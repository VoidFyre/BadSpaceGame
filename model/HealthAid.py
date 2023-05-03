import pygame
import os

class HealthAid:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.ship_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "first_aid.png")).convert_alpha(),
                               (30, 30))
        self.mask = pygame.mask.from_surface(self.ship_img)

        # Load the sound file
        self.sound = pygame.mixer.Sound(os.path.join("assets", "sounds/health_pack.wav"))

    def move(self, vel):
        self.y += vel

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def play_sound(self):
        # Play the sound
        self.sound.play()
