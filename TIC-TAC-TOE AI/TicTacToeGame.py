class TicTacToeGame:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "O"
        self.ai_player = "X"  # Set AI player to "X"
        self.human_player = "O"  # Set human player to "O"
        self.winning_combinations = [
            [0, 1, 2],  # rows
            [3, 4, 5],  # rows
            [6, 7, 8],  # rows
            [0, 3, 6],  # cols
            [1, 4, 7],  # cols
            [2, 5, 8],  # cols
            [0, 4, 8],  # diagonals
            [2, 4, 6],  # diagonals
        ]
        self.winning_combination = []

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player

    def change_player(self):
        self.current_player = (
            self.ai_player
            if self.current_player == self.human_player
            else self.human_player
        )

    def check_winner(self):
        for combination in self.winning_combinations:
            if all(self.board[i] == self.ai_player for i in combination):
                self.winning_combination = combination  # Save the winning combination
                return "AI"  # Indicate AI wins
            elif all(self.board[i] == self.human_player for i in combination):
                self.winning_combination = combination  # Save the winning combination
                return "Human"  # Indicate Human wins
        return None  # No winner yet

    def is_draw(self):
        return " " not in self.board

    def get_empty_cells(self):
        return [i for i, cell in enumerate(self.board) if cell == " "]

    def get_current_player(self):
        return self.current_player

    def get_winning_combination(self):
        return self.winning_combination
