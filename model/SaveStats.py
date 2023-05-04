class SaveStats:
    def __init__(self, game_state):
        # Initialize high score and total kills to 0
        # self.high_score = 0
        # self.total_kills = 0

        self.game_state = game_state

        # Load high score and total kills from a text file
        try:
            with open("scores.txt", "r") as f:
                lines = f.readlines()
                self.game_state.high_score_counter = int(lines[0].split(":")[1].strip())
                self.game_state.high_total_killing = int(lines[1].split(":")[1].strip())
        except FileNotFoundError:
            self.game_state.high_score_counter = 0
            self.game_state.high_total_killing = 0

    def end_game(self):
        # Update high score and total kills
        if self.game_state.high_score_counter < self.game_state.score_counter:
            self.game_state.high_score_counter = self.game_state.score_counter
        if self.game_state.high_total_killing < self.game_state.total_killing:
            self.game_state.high_total_killing = self.game_state.total_killing

        # Save high score and total kills to a text file
        with open("scores.txt", "w") as f:
            f.write(f"High score: {self.game_state.high_score_counter}\n")
            f.write(f"Total kills: {self.game_state.high_total_killing}\n")
