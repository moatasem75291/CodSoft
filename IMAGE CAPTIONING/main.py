from PyQt5.QtWidgets import QApplication
from gui_app import ImageCaptioningApp


def main():
    app = QApplication([])
    window = ImageCaptioningApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
