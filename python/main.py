from controller.game_controller import Game

class Main:
    def main(self):
        self.g = Game()

        while self.g.running:
            self.g.curr_menu.display_menu()
            self.g.game_loop()

if __name__ == "__main__":
    Main().main()
