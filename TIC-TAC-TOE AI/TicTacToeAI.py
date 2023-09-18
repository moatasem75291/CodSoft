import math
import random


class TicTacToeAI:
    def __init__(self, game):
        self.game = game

    def minimax(self, depth, is_maximizing, alpha, beta):
        if self.game.check_winner():
            if self.game.get_current_player() == "X":
                return -1
            else:
                return 1
        elif self.game.is_draw():
            return 0

        if is_maximizing:
            best_val = -math.inf
            for move in self.game.get_empty_cells():
                self.game.make_move(move)
                move_val = self.minimax(depth + 1, False, alpha, beta)
                self.game.board[move] = " "  # Undo the move
                best_val = max(best_val, move_val)
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break
            return best_val
        else:
            best_val = math.inf
            for move in self.game.get_empty_cells():
                self.game.make_move(move)
                move_val = self.minimax(depth + 1, True, alpha, beta)
                self.game.board[move] = " "  # Undo the move
                best_val = min(best_val, move_val)
                beta = min(beta, best_val)
                if beta <= alpha:
                    break
            return best_val

    def best_move(self):
        empty_cells = self.game.get_empty_cells()
        random_move = (
            random.choice(empty_cells) if empty_cells else -1
        )  # Select a random move if available, otherwise -1
        empty_cells = random.sample(empty_cells, len(empty_cells))
        best_val = -math.inf
        best_move = -1
        alpha = -math.inf
        beta = math.inf

        for move in empty_cells:
            self.game.make_move(move)
            if self.game.check_winner() == "O":
                # If 'O' can win in the next move, make that move and return it.
                self.game.board[move] = "O"
                return move
            move_val = self.minimax(0, True, alpha, beta)
            self.game.board[move] = " "  # Undo the move
            if move_val > best_val:
                best_val = move_val
                best_move = move
            alpha = max(alpha, best_val)

        if best_move != -1:
            return best_move

        # If there's no immediate winning move, return a random move.
        return random_move
