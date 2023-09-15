from PyQt5.QtWidgets import (
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMainWindow,
    QLabel,
)
from PyQt5.QtGui import QTextCursor, QColor, QFont
from PyQt5.QtCore import Qt


class ChatbotGUI(QMainWindow):
    def __init__(self, model):
        super().__init__()

        self.model = model
        self.first_run = True

        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Nemo Chatbot")
        self.setGeometry(300, 300, 700, 700)

        layout = QVBoxLayout()

        # Welcome message label
        if self.first_run:
            welcome_label = QLabel(
                "Welcome! I'm Nemo, your chatbot. How can I assist you today?", self
            )
            welcome_label.setAlignment(Qt.AlignCenter)
            welcome_label.setStyleSheet(
                "background-color: #B0A4A4; color: #000; font-size: 16px; padding: 10px; border-radius: 5px;"
            )
            layout.addWidget(welcome_label)
            self.first_run = False

        self.input_text = QTextEdit(self)
        self.input_text.setFont(QFont("Arial", 15))  # font size
        self.input_text.setFixedSize(700, 125)
        self.input_text.setStyleSheet(
            "background-color: #f2f2f2; color: #333; border: 2px solid #ccc; border-radius: 5px;"
        )
        layout.addWidget(self.input_text)

        self.chat_display = QTextEdit(self)
        self.chat_display.setFont(QFont("", 24))
        self.chat_display.setStyleSheet(
            "background-color: #5F264A; border: 2px solid #ccc; border-radius: 5px;"
        )
        self.chat_display.setTextColor(QColor(0, 0, 0))
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)

        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.process_input)
        self.send_button.setStyleSheet(
            "background-color: #643A6B; color: white; border: none; border-radius: 10px; padding: 10px 20px; font-size: 16px;"
        )
        layout.addWidget(self.send_button)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.clear_chat)
        self.clear_button.setStyleSheet(
            "background-color: #957777; color: white; border: none; border-radius: 10px; padding: 10px 20px; font-size: 16px;"
        )
        layout.addWidget(self.clear_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def process_input(self):
        user_input = self.input_text.toPlainText()
        nemo_response = self.model.query(user_input)
        self.chat_display.moveCursor(QTextCursor.End)

        self.chat_display.setTextColor(QColor(255, 255, 255))
        self.chat_display.setFontWeight(QFont.Normal)
        self.chat_display.insertPlainText(f"User: {user_input}\n")

        self.chat_display.setTextColor(QColor("#FFC6AC"))
        self.chat_display.setFontWeight(QFont.Bold)
        self.chat_display.insertPlainText(f"Nemo: {nemo_response}\n")
        self.input_text.clear()

    def clear_chat(self):
        self.chat_display.clear()
