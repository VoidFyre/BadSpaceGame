import pygame
import os


class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Create a timer for enemy shooting
        self.explosion_shoot_timer = pygame.time.get_ticks()

        self.explosion_image = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "component/secondary/explosion/explosion_secondary_common.png")).convert_alpha(),
            (70, 70))
        self.mask = pygame.mask.from_surface(self.explosion_image)

        # Load the sound file
        self.sound = pygame.mixer.Sound(os.path.join("assets", "sounds/sounds_powerup.wav"))

    # def update(self, dt):
    #     self.opacity -= dt / 5.0  # Decrease opacity over 5 seconds
    #     if self.opacity <= 0.0:
    #         self.opacity = 0.0

    # def draw(self, surface):
    #     alpha = int(self.opacity * 255)  # Convert opacity to alpha value (0-255)
    #     self.image.set_alpha(alpha)  # Set the alpha value of the image
    #     surface.blit(self.image, self.rect)
    #
    def move(self, vel):
        self.y += vel

    def draw(self, window):

        print("window: ", window, self.explosion_image)
        window.blit(self.explosion_image, (self.x, self.y))

    def get_width(self):
        return self.explosion_image.get_width()

    def get_height(self):
        return self.explosion_image.get_height()

    def play_sound(self):
        # Play the sound
        self.sound.play()

