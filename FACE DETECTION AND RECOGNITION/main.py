import sys
from PyQt5.QtWidgets import QApplication
from faceDetection_gui import FaceDetectionApp


def main():
    app = QApplication(sys.argv)
    window = FaceDetectionApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
