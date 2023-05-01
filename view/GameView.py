import pygame
from view.SpaceshipView import SpaceshipView
from view.EnemyView import EnemyView
from view.UpgradeView import UpgradeView

class GameView:
    def __init__(self, width, height):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Bad Things in Outer Space, the Game")
        self.background = pygame.image.load("./assets/interface/inventory_screen.png")
        self.font = pygame.font.SysFont("Arial", 24)
        self.sound_effects = {
            # 'explosion': pygame.mixer.Sound('assets/sounds/explosion.wav'),
            # 'powerup': pygame.mixer.Sound('./assets/sounds/powerup.wav')
        }

        #self.menu_view = Menu()
        self.spaceship_view = SpaceshipView()
        self.enemy_view = EnemyView()
        self.powerup_view = UpgradeView()

    def drawMenu(self, game):
        return

    def draw(self, model):
        self.screen.blit(self.background, (0, 0))

        # Draw spaceship
        self.spaceship_view.draw(self.screen, model.spaceship)

        # Draw enemies
        for enemy in model.enemies:
            self.enemy_view.draw(self.screen, enemy)

        # Draw power-ups
        for powerup in model.powerups:
            self.powerup_view.draw(self.screen, powerup)

        # Draw score
        score_text = self.font.render("Score: {}".format(model.score), True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        # Draw health
        health_text = self.font.render("Health: {}".format(model.spaceship.health), True, (255, 255, 255))
        self.screen.blit(health_text, (10, 40))

        pygame.display.update()

    def play_sound_effect(self, effect_name):
        self.sound_effects[effect_name].play()
