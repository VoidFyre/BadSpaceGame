import pygame
from controller.GameController import GameController
from view.GameView import GameView
from model.GameModel import GameModel

def main():
    # Set up the game window and clock
    width = 800
    height = 600
    game_view = GameView(width, height)
    clock = pygame.time.Clock()

    # Set up the game model and controller
    game_model = GameModel()
    game_controller = GameController(game_model, game_view)

    # Run the game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # game_controller.handle_event(event)

        # Update the game state
        game_controller.update()

        # Draw the game
        game_view.draw(game_model.game_state)

        # Limit the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
