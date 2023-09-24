from feature_extraction import FeatureExtractor
from caption_generation import CaptionGenerator
from prepared_captions import PreparedCaptions
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
)


class ImageCaptioningApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Captioning App")
        self.setGeometry(600, 300, 900, 600)
        self.font = QFont()

        self.initUI()

    def initUI(self):
        # Create widgets
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.caption_label = QLabel(self)
        self.caption_label.setAlignment(Qt.AlignCenter)
        self.upload_button = QPushButton("Upload Image", self)
        self.upload_button.clicked.connect(self.openImageDialog)

        # Style and appearance customization
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #dedede; /* Light gray background */
                border: 6px solid #fff; /* Add a border to make the background more prominent */
                font-family: Arial;
                font-size: 20px;
            }
            QPushButton {
                background-color: #4CAF50; /* Green background */
                color: white;
                padding: 10px 20px;
                font-size: 24px;
                border: none;
                border-radius: 15px;
                font-family: Arial;
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker green background on hover */
            }
            """
        )

        # Layout
        main_layout = QVBoxLayout()
        image_layout = QVBoxLayout()
        caption_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.font.setPointSize(
            14
        )  # Set font size to 13 for the image layout, and the caption layout

        label_uploaded_image = QLabel("Uploaded Image")
        label_uploaded_image.setFont(self.font)
        image_layout.addWidget(label_uploaded_image)
        image_layout.addWidget(self.image_label)

        label_generate_caption = QLabel("Generated Caption")
        label_generate_caption.setFont(self.font)
        caption_layout.addWidget(label_generate_caption)
        caption_layout.addWidget(self.caption_label)

        button_layout.addWidget(self.upload_button)

        main_layout.addLayout(image_layout)
        main_layout.addLayout(caption_layout)
        main_layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.image_path = None
        self.model_path = r"C:\Users\MBR\Desktop\Internships\CodSoft\CodSoft\IMAGE CAPTIONING\best_model.h5"
        self.caption_path = r"C:\Users\MBR\Desktop\Internships\CodSoft\CodSoft\IMAGE CAPTIONING\captions.txt"

    def openImageDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image File",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)",
            options=options,
        )

        if file_path:
            print(file_path)
            self.image_path = file_path
            self.displayImage(file_path)

            # # Generate caption
            self.generateCaption()

    def displayImage(self, image_path):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(400)  # Increased image width
        self.image_label.setPixmap(pixmap)

    def generateCaption(self):
        if self.image_path:
            # Extract image features
            feature_extractor = FeatureExtractor()
            image_features = feature_extractor.extract_image_features(self.image_path)

            # Tokenize captions
            prepared_captions = PreparedCaptions(self.caption_path)
            tokenizer, max_caption_length = prepared_captions.tokenize_captions()

            # Generate caption
            caption_generator = CaptionGenerator(
                self.model_path, tokenizer, max_caption_length
            )
            caption = caption_generator.generate_caption(image_features)

            caption = caption.replace("start ", "").replace(
                " end", ""
            )  # Remove the "start" and "end" keywords from the generated caption

            # Set the caption text in the QLabel
            self.caption_label.setText(caption)
            self.caption_label.setStyleSheet("color: #000; font-size: 22px;")
