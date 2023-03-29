import pygame
import pygame_gui
import os

from controller.GameController import GameController
from model.GameState import GameState

pygame.init()

# Set up the Pygame window
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Menu View")

# Set up the background image
background_image = pygame.image.load(os.path.join("assets", "space_background_2.png"))

# Create the GUI manager
gui_manager = pygame_gui.UIManager(window_size)

# Create the buttons
start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((220, 225), (200, 50)),
    text="Start",
    manager=gui_manager
)

options_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((220, 300), (200, 50)),
    text="Options",
    manager=gui_manager
)

credits_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((220, 375), (200, 50)),
    text="Credits",
    manager=gui_manager
)

level1_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((220, 225), (200, 50)),
    text="Level 1",
    manager=gui_manager,
    visible=False
)

level2_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((440, 225), (200, 50)),
    text="Level 2",
    manager=gui_manager,
    visible=False
)

level3_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((660, 225), (200, 50)),
    text="Level 3",
    manager=gui_manager,
    visible=False
)

back_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 10), (100, 30)),
    text="Back",
    manager=gui_manager,
    visible=False
)

# Run the game loop
clock = pygame.time.Clock()
is_running = True


def start_game():
    # Set up the game window and clock
    height = 750
    width = 750

    game_state = GameState(width, height)

    game_state.playing = True

    game_controller = GameController(game_state, None, None)

    #menu_view = Menu(self.game_state)

    game_controller.run_game_loop()

while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    start_button.kill()
                    options_button.kill()
                    credits_button.kill()
                    level1_button.visible = True
                    level2_button.visible = True
                    level3_button.visible = True
                    back_button.visible = True

                elif event.ui_element == level1_button:
                    pygame.quit()
                    start_game()  # This is where you would call your game function

                elif event.ui_element == back_button:
                    level1_button.visible = False
                    level2_button.visible = False
                    level3_button.visible = False
                    back_button.visible = False
                    start_button.visible = True
                    options_button.visible = True
                    credits_button.visible = True

                # Add code to handle the other level buttons here

        gui_manager.process_events(event)

    gui_manager.update(time_delta)
    screen.blit(background_image, (0, 0))
    gui_manager.draw_ui(screen)
    pygame.display.update()

pygame.quit()





