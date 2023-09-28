from face_detector import FaceDetector
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QComboBox,
    QLabel,
)
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtCore import Qt
import cv2
import threading


class FaceDetectionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.font = QFont()
        self.font.setPointSize(16)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Face Detection")
        self.setGeometry(500, 300, 800, 600)

        # Customize the background color of the central widget
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet("background-color: lightgray;")
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFont(self.font)

        self.detect_button = QPushButton("Detect Faces", self)
        self.stop_button = QPushButton("Stop Detection", self)

        self.detect_button.clicked.connect(self.change_source)
        self.detect_button.setStyleSheet(
            "background-color: green; color: white; font-size: 20px;"
        )
        self.stop_button.clicked.connect(self._stop_detection)
        self.stop_button.setStyleSheet(
            "background-color: red; color: white; font-size: 20px;"
        )

        self.choose_source_label = QLabel("Choose source:", self)
        self.choose_source_label.setFont(self.font)

        self.source_combobox = QComboBox(self)
        self.source_combobox.setFont(self.font)
        self.source_combobox.addItem("Camera")
        self.source_combobox.addItem("Image/Video")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.choose_source_label)
        self.layout.addWidget(self.source_combobox)
        self.layout.addWidget(self.detect_button)
        self.layout.addWidget(self.stop_button)

        self.central_widget.setLayout(self.layout)

        self.cap = None
        self.face_detector = FaceDetector()
        self.detection_active = True

    def change_source(self):
        source = self.source_combobox.currentText()

        if source == "Camera":
            self._open_camera()
        elif source == "Image/Video":
            self._open_file()

    def _stop_detection(self):
        self.detection_active = False  # Set the flag to stop detection

    def _open_camera(self):
        self.cap = cv2.VideoCapture(0)

        def camera_worker():
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break

                frame_with_faces = self.face_detector.detect_faces(frame)
                self._display_frame(frame_with_faces)

                if cv2.waitKey(1) & 0xFF == ord("q") or not self.detection_active:
                    self.detection_active = True
                    break

            self.cap.release()
            cv2.destroyAllWindows()

        camera_thread = threading.Thread(target=camera_worker)
        camera_thread.start()

    def _open_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Open Image/Video File",
            "",
            "Video Files (*.mp4 *.avi);;Image Files (*.jpg *.jpeg *.png)",
        )
        if file_path:
            if file_path.endswith((".mp4", ".avi")):
                self.cap = cv2.VideoCapture(file_path)

                while True:
                    ret, frame = self.cap.read()
                    if not ret:
                        break

                    frame_with_faces = self.face_detector.detect_faces(frame)
                    self._display_frame(frame_with_faces)

                    if cv2.waitKey(1) & 0xFF == ord("q") or not self.detection_active:
                        self.detection_active = True
                        break
                self.cap.release()
                cv2.destroyAllWindows()
            elif file_path.endswith((".jpg", ".jpeg", ".png")):
                image = cv2.imread(file_path)
                frame_with_faces = self.face_detector.detect_faces(image)
                self._display_frame(frame_with_faces)

    def _display_frame(self, frame):
        q_image = QImage(
            frame.data,
            frame.shape[1],
            frame.shape[0],
            frame.shape[1] * 3,
            QImage.Format_BGR888,
        )
        pixmap = QPixmap.fromImage(q_image)
        self.image_label.setPixmap(pixmap)
