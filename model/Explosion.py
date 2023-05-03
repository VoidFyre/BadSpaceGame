import pygame
import os

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None

class Explosion:
    def __init__(self, x, y, img, size):
        self.x = x
        self.y = y
        self.type = "ship"
        self.collide = True

        # Create a timer for enemy shooting
        self.explosion_shoot_timer = pygame.time.get_ticks()

        self.explosion_image = pygame.transform.scale(
            img.convert_alpha(),
            size)
        self.mask = pygame.mask.from_surface(self.explosion_image)

        # Load the sound file
        self.sound = pygame.mixer.Sound(os.path.join("assets", "sounds/explosion.wav"))

    def move(self, vel):
        self.y += vel

    def draw(self, window):
        
        if self.type == "ship":
            window.blit(self.explosion_image, (self.x, self.y))
        
        if self.type == "weapon":
            window.blit(self.explosion_image, (self.x, self.y))

    def get_width(self):
        return self.explosion_image.get_width()

    def get_height(self):
        return self.explosion_image.get_height()

    def play_sound(self):
        # Play the sound
        self.sound.play()

    def collision(self, obj):
        return collide(self, obj)

