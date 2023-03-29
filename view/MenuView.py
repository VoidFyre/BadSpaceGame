import pygame
from os.path import abspath


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

        self.background_image = pygame.image.load(abspath('assets/interface/inventory_screen.png'))
        self.background_image = pygame.transform.scale(self.background_image , (self.game.DISPLAY_W, self.game.DISPLAY_H))

    def draw_cursor(self):
        self.game.draw_text('->', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 60
        self.quitx, self.quity = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()

            # Draw background image
            self.game.display.blit(self.background_image, (0, 0))
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.game.draw_text("Quit", 20, self.quitx, self.quity)
            self.draw_cursor()
            self.blit_screen()



    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            print("state: ", self.state)
            if self.state == 'Start':
                self.game.curr_menu = self.game.start
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Quit':
                self.game.running, self.game.playing = False, False
            self.run_display = False

class StartMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Level 1'
        self.splayerx, self.splayery = self.mid_w, self.mid_h + 20
        self.mplayerx, self.mplayery = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.splayerx + self.offset, self.splayery)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()

            # Draw background image
            self.game.display.blit(self.background_image, (0, 0))
            self.game.draw_text('Start', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Level 1", 15, self.splayerx, self.splayery)
            self.game.draw_text("Level 2", 15, self.mplayerx, self.mplayery)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.ESCAPE_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Level 1':
                self.state = 'Level 2'
                self.cursor_rect.midtop = (self.splayerx + self.offset, self.splayery)
            elif self.state == 'Level 2':
                self.state = 'Level 1'
                self.cursor_rect.midtop = (self.mplayerx + self.offset, self.mplayerx)
        elif self.game.START_KEY:
            print("states:", self.state)
            if self.state == 'Level 1':
                self.game.single_player = True
                self.game.playing = True
            elif self.state == 'Level 2':
                self.game.single_player = False
                self.game.playing = True
            self.run_display = False
            pass



class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            # Draw background image
            self.game.display.blit(self.background_image, (0, 0))
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made with lots of love <3', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()