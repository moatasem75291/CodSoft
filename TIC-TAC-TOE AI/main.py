import sys
from PyQt5.QtWidgets import QApplication
from TicTacToeGUI import TicTacToeGUI


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToeGUI()
    window.show()
    sys.exit(app.exec_())
