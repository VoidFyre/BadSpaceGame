import pygame
import os

class GameState:
    __instance = None  # class variable to hold the singleton instance

    def __init__(self, width=700, height=500):

        pygame.init()
        pygame.display.set_caption("Bad things in outer Space, the Game")

        self.FPS = 60
        self.level = 0

        self.enemies = []
        self.healthAids = []
        self.upgrades = []
        self.wave_length = 5
        self.enemy_vel = 1
        self.healthAids_vel = 1
        self.upgrades_vel = 1

        self.explosions = []

        self.player_vel = 3
        self.laser_vel = 5

        self.lost = False
        self.lost_count = 0

        self.score_counter = 0
        self.total_killing = 0

        self.high_score_counter = 0
        self.high_total_killing = 0

        self.running, self.playing, self.game_over, self.pause = True, False, False, False

        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY, self.SPACE_KEY = False, False, False, False, False, False

        self.DISPLAY_W, self.DISPLAY_H = width, height

        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))

        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))

        #self.font_name = pygame.font.get_default_font()

        self.main_font = pygame.font.Font(os.path.join("assets", "fonts/munro.ttf"), 30)

        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        self.clock = pygame.time.Clock()

        self.current_menu_button = None

        self.player_current_ship = "common"

        self.player_current_primary = "common"

        self.player_current_secondary = "common"

        self.player_current_thruster = "common"

        # Background
        self.BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "space_background_9.png")).convert_alpha(), (self.DISPLAY_W, self.DISPLAY_H))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
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


    def game_reset(self, width=700, height=500):

        self.level = 0

        self.enemies = []
        self.healthAids = []
        self.upgrades = []
        self.wave_length = 5
        self.enemy_vel = 1

        self.explosions = []

        self.player_vel = 5
        self.laser_vel = 5

        self.lost = False
        self.lost_count = 0

        self.score_counter = 0
        self.total_killing = 0

        self.player_current_ship = "common"

        self.player_current_primary = "common"

        self.player_current_secondary = "common"

        self.player_current_thruster = "common"

        self.running, self.playing, self.game_over, self.pause = True, True, False, False

        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY, self.SPACE_KEY = False, False, False, False, False, False

        self.current_menu_button = None

    def enable_music(self, enable=True):
        if enable:
            pygame.mixer.music.load(os.path.join("assets", "sounds/background_music.ogg"))
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()
