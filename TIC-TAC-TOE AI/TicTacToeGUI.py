from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from TicTacToeGame import TicTacToeGame
from TicTacToeAI import TicTacToeAI


class TicTacToeGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(600, 300, 450, 450)
        self.game = TicTacToeGame()
        self.ai = TicTacToeAI(self.game)
        self.buttons = [QPushButton("", self) for _ in range(9)]
        self.font = QFont()
        self.font.setPointSize(20)
        self.setup_buttons()

    def setup_buttons(self):
        for i, button in enumerate(self.buttons):
            button.resize(150, 150)
            button.move((i % 3) * 150, (i // 3) * 150)
            button.clicked.connect(lambda _, idx=i: self.handle_click(idx))

    def handle_click(self, position):
        if (
            self.game.check_winner()
            or self.game.is_draw()
            or self.game.board[position] != " "
        ):
            return
        self.game.make_move(position)  # Make the move
        self._setup_board(position)  # Update the GUI
        self.game.change_player()  # Change the player
        winner = self.game.check_winner()  # Check if there's a winner
        if winner is not None:
            self._winner(winner)  # If there's a winner, show the winner
        elif self.game.is_draw():
            QMessageBox.information(self, "Game Over", "It's a Draw!")
            self.reset_game()
        else:
            self.ai_move()  # If there's no winner, let AI make a move

    def ai_move(self):
        ai_position = self.ai.best_move()
        self.game.make_move(ai_position)
        self._setup_board(ai_position)
        self.game.change_player()
        winner = self.game.check_winner()
        if winner is not None:
            self._winner(winner)
        elif self.game.is_draw():
            QMessageBox.information(self, "Game Over", "It's a Draw!")
            self.reset_game()

    def _winner(self, winner):
        winning_combination = self.game.get_winning_combination()
        if winner == "Human":
            color = "green"
        elif winner == "AI":
            color = "red"

        for index in winning_combination:
            self.buttons[index].setStyleSheet(f"background-color: {color};")
        QMessageBox.information(self, "Game Over", f"{winner} wins!")
        self.reset_game()

    def _setup_board(self, position):
        self.buttons[position].setText(self.game.get_current_player())
        self.buttons[position].setFont(self.font)

    def reset_game(self):
        for button in self.buttons:
            button.setText("")
            button.setStyleSheet("background-color: white;")
        self.game = TicTacToeGame()
        self.ai = TicTacToeAI(self.game)
