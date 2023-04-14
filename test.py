__all__ = ['main']

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Optional

# Constants and global variables
FPS = 60
WINDOW_SIZE = (750, 750)

sound: Optional['pygame_menu.sound.Sound'] = None
surface: Optional['pygame.Surface'] = None
main_menu: Optional['pygame_menu.Menu'] = None

# Load image
background_image = pygame_menu.BaseImage(
    image_path='/Users/macbookair/PycharmProjects/BadSpaceGame/assets/space_background_9.png'

)

background_image2 = pygame_menu.BaseImage(
    image_path='/Users/macbookair/PycharmProjects/BadSpaceGame/assets/space_background_10.png'

)

def main_background() -> None:
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.
    """
    background_image.draw(surface)


def main(test: bool = False) -> None:
    """
    Main program.
    :param test: Indicate function is being tested
    """
    global main_menu
    global sound
    global surface

    # Create window
    surface = create_example_window('Example - Image Background', WINDOW_SIZE)
    clock = pygame.time.Clock()

    # Create menus: Main menu
    main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    main_menu_theme.set_background_color_opacity(0.5)  # 50% opacity

    main_menu_theme.background_color = background_image2
    main_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
    main_menu_theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
    main_menu_theme.widget_font = pygame_menu.font.FONT_MUNRO
    #main_menu_theme.widget_selection_effect = pygame_menu.widgets.RightArrowSelection
    main_menu_theme.widget_margin = (0, 20)
    main_menu_theme.widget_offset = (40, 0)
    main_menu_theme.title_offset = (20, 10)
    main_menu_theme.title_font = pygame_menu.font.FONT_MUNRO
    main_menu_theme.selection_effect = pygame_menu.widgets.RightArrowSelection()

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.6,
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        theme=main_menu_theme,
        title='Menu',
        width=WINDOW_SIZE[0] * 0.7,
    )


    theme_bg_image = main_menu_theme.copy()
    theme_bg_image.background_color = pygame_menu.BaseImage(
        image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_CARBON_FIBER
    )
    theme_bg_image.title_font_size = 25
    menu_with_bg_image = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.6,
        onclose=pygame_menu.events.EXIT,
        theme=theme_bg_image,
        title='Menu with background image',
        width=WINDOW_SIZE[0] * 0.7
    )
    menu_with_bg_image.add.button('Back', pygame_menu.events.BACK)
    menu_with_bg_image.widget_font = pygame_menu.font.FONT_MUNRO

    widget_colors_theme = pygame_menu.themes.THEME_DARK.copy()
    widget_colors_theme.widget_margin = (0, 10)
    widget_colors_theme.widget_padding = 0
    widget_colors_theme.widget_selection_effect.margin_xy(10, 5)
    widget_colors_theme.widget_font_size = 20
    widget_colors_theme.set_background_color_opacity(0.5)  # 50% opacity
    widget_colors_theme.background_color = background_image
    widget_colors_theme.widget_font = pygame_menu.font.FONT_MUNRO
    #widget_colors_theme.widget_selection_effect = pygame_menu.widgets.RightArrowSelection

    widget_colors = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        theme=widget_colors_theme,
        title='',
        width=WINDOW_SIZE[0] * 0.8
    )

    widget_colors.add.label('Made with lots of love <3')

    main_menu.add.button('Play', menu_with_bg_image, align=pygame_menu.locals.ALIGN_LEFT)
    main_menu.add.button('Credit', widget_colors, align=pygame_menu.locals.ALIGN_LEFT)
    main_menu.add.button('Quit', pygame_menu.events.EXIT, align=pygame_menu.locals.ALIGN_LEFT)

    # Main loop
    while True:

        # Tick
        clock.tick(FPS)

        # Main menu
        main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()