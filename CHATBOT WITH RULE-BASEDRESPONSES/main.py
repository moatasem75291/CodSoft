import sys
from PyQt5.QtWidgets import QApplication
from chatbot_gui import ChatbotGUI
from model import ChatbotModel


def main():
    app = QApplication(sys.argv)
    model = ChatbotModel()
    chatbot = ChatbotGUI(model)
    chatbot.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
