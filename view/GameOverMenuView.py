import pygame
import pygame_menu
import os

class GameOverMenuView:
    WINDOW_SIZE = (750, 750)
    FPS = 60
    test = False

    def __init__(self):

        self.label_text = True
        self.game_state = None

        # Load background images
        self.main_background_image = pygame_menu.BaseImage(image_path=os.path.join("assets", "space_background_9.png"))
        self.menu_background_image = pygame_menu.BaseImage(image_path=os.path.join("assets", "space_background_10.png"))

        # Create themes
        main_menu_theme = self._create_main_menu_theme()
        widget_colors_theme = self._create_widget_colors_theme()

        # Create menus
        self.main_menu = pygame_menu.Menu(
            height=self.WINDOW_SIZE[1] * 0.6,
            onclose=pygame_menu.events.EXIT,  # User press ESC button
            theme=main_menu_theme,
            title='Game Over',
            width=self.WINDOW_SIZE[0] * 0.7,
        )

        #self.widget_colors = self._create_widget_colors(theme=widget_colors_theme)

        # Add buttons to main menu
        self.main_menu.add.button('Restart', self.restart_callback, align=pygame_menu.locals.ALIGN_LEFT)
        self.main_menu.add.button('Main Menu', self.main_menu_callback, align=pygame_menu.locals.ALIGN_LEFT)
        self.main_menu.add.button('Quit', pygame_menu.events.EXIT, align=pygame_menu.locals.ALIGN_LEFT)

    def restart_callback(self):
        # Do something when the play button is clicked
        # self.game_state.pause = False
        self.game_state.current_menu_button = "Restart"

        self.game_state.lost = False
        self.game_state.playing = True

        print(self.game_state.current_menu_button , self.game_state.lost)

    def main_menu_callback(self):
        # Do something when the play button is clicked
        self.game_state.current_menu_button = "Main Menu"

        self.game_state.lost = False

    def _create_main_menu_theme(self):
        theme = pygame_menu.themes.THEME_DARK.copy()
        theme.set_background_color_opacity(0.2)  # 50% opacity
        theme.background_color = self.menu_background_image
        theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
        theme.widget_font = pygame_menu.font.FONT_MUNRO
        theme.widget_margin = (0, 20)
        theme.widget_offset = (40, 0)
        theme.title_offset = (20, 10)
        theme.title_font = pygame_menu.font.FONT_MUNRO
        theme.title_font_size = 30
        theme.selection_effect = pygame_menu.widgets.RightArrowSelection()
        return theme

    def _create_play_menu_button(self, theme):
        menu = pygame_menu.Menu(
            height=self.WINDOW_SIZE[1] * 0.6,
            onclose=pygame_menu.events.EXIT,
            theme=theme,
            title='Menu with background image',
            width=self.WINDOW_SIZE[0] * 0.7

        )
        menu.add.button('Back', pygame_menu.events.BACK)
        menu.widget_font = pygame_menu.font.FONT_MUNRO
        menu.set_onupdate(self.main_menu_callback)
        return menu

    def _create_widget_colors_theme(self):
        theme = pygame_menu.themes.THEME_DARK.copy()
        theme.widget_margin = (0, 10)
        theme.widget_padding = 0
        theme.widget_selection_effect.margin_xy(10, 5)
        theme.widget_font_size = 20
        theme.set_background_color_opacity(0.2)  # 50% opacity
        theme.background_color = self.main_background_image
        theme.widget_font = pygame_menu.font.FONT_MUNRO
        return theme

    def _create_widget_colors(self, theme):
        menu = pygame_menu.Menu(
            height=self.WINDOW_SIZE[1] * 0.7,
            theme=theme,
            title='',
            width=self.WINDOW_SIZE[0] * 0.8
        )
        menu.add.label('Made with lots of love <3')
        return menu

    def main_background(self) -> None:
        """
        Background color of the main menu, on this function user can plot
        images, play sounds, etc.
        """
        self.main_background_image.draw(self.game_state.window)

    def set_game_state(self, game_state):
        self.game_state = game_state

    def run(self):

        self.main_menu.mainloop(self.game_state.window, self.main_background, disable_loop = self.game_state.lost,
                                fps_limit=self.FPS)
        # Flip surface
        pygame.display.flip()

