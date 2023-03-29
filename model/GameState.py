import pygame
import os

from view.MenuView import MainMenu, StartMenu, CreditsMenu

from model.Spaceship import Spaceship


class GameState:
    __instance = None  # class variable to hold the singleton instance

    def __init__(self, width=700, height=500):

        pygame.init()
        pygame.display.set_caption("Bad Space Game")

        self.FPS = 60
        self.level = 0
        self.lives = 5
        self.main_font = pygame.font.SysFont("comicsans", 50)
        self.lost_font = pygame.font.SysFont("comicsans", 60)

        self.enemies = []
        self.wave_length = 5
        self.enemy_vel = 1

        self.player_vel = 5
        self.laser_vel = 5

        self.lost = False
        self.lost_count = 0

        self.running, self.playing, self.game_over = True, False, False

        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY, self.SPACE_KEY = False, False, False, False, False, False

        self.DISPLAY_W, self.DISPLAY_H = width, height

        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))

        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))

        self.font_name = pygame.font.get_default_font()

        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        self.main_menu = MainMenu(self)
        self.start = StartMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

        self.clock = pygame.time.Clock()

        # Load images
        self.RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
        self.GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
        self.BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

        # Player player
        self.YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

        # Lasers
        self.RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
        self.GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
        self.BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
        self.YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

        # Background
        self.BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (self.DISPLAY_W, self.DISPLAY_H))

        self.BG_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "space_background_1.png")),
                                         (self.DISPLAY_W, self.DISPLAY_H))
        self.BG_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "space_background_2.png")),
                                           (self.DISPLAY_W, self.DISPLAY_H))

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)

        text_surface = font.render(text, True, (255, 20, 123))
        shadow = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(x, y))
        shadow_rect = text_surface.get_rect(center=(x + 2, y + 2))
        self.display.blit(shadow, shadow_rect)
        self.display.blit(text_surface, text_rect)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY = True
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY, self.SPACE_KEY = False, False, False, False, False, False
