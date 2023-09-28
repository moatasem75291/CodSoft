# CodSoft Internship Project: Face Detection App with PyQt5 GUI

This project is a Face Detection Application created using Python, OpenCV, and PyQt5. It allows users to perform real-time face detection using a webcam or analyze images and video files.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Customization](#customization)

## Overview

Our CodSoft internship project presents a Face Detection Application featuring a user-friendly PyQt5-based graphical user interface (GUI). With this application, users can easily perform real-time face detection using their webcam or analyze images and video files for face detection.

## Getting Started

### Prerequisites

Before you start using this project, ensure you have the following installed:

- Python (3.7 or higher)
- OpenCV (for image processing)
- PyQt5 (for the graphical user interface)

## Project Structure

The project is organized as follows:

- `main.py`: This serves as the primary application script and is responsible for initializing the PyQt5 GUI and managing user interactions.

- `faceDetection_gui.py`: This script defines the PyQt5-based graphical user interface for image and video source selection, as well as starting and stopping face detection.

- `face_detector.py`: In this module, you'll find the `FaceDetector` class, which utilizes OpenCV to detect faces in images and video frames.

- `README.md`: You're currently reading this documentation file, which provides an overview of the project, instructions, and information on its structure.

Feel free to explore each component to gain a deeper understanding of the project's organization and functionality.

## Usage

To make the most of the application, follow these simple steps:

**1. Launch the Application: Start the application by running the following command in your terminal or command prompt:

   ```bash
   python main.py
  ```

**2. Exploring the GUI:**
Upon launching the application, you will be presented with a graphical user interface (GUI). The GUI prominently provides the following options:

- Selecting the Image/Video Source
- Buttons for Initiating and Stopping Face Detection

**3. Selecting the Source:**
Utilize the "Choose source" combo box to specify your desired source:

- "Camera": Select this option to perform real-time face detection using your webcam.
- "Image/Video": Choose this option to analyze face detection in image or video files. You will be prompted to select a file for analysis.

**4. Initiating Face Detection:**
To begin the face detection process, click the "Detect Faces" button. The behavior depends on your source selection:

- If you chose "Camera," the application will immediately start real-time face detection from your webcam.
- If you selected "Image/Video," you will be prompted to select a file for analysis, and the application will proceed to detect faces within it.

**5. Stopping Face Detection:**
At any point during the detection process, you can halt the face detection by clicking the "Stop Detection" button.

**6. Enjoy Face Detection:**
The application will display either the live video feed (in the case of webcam usage) or the image/video with detected faces outlined by green rectangles. This visual representation provides a clear and intuitive view of the detected faces.

These straightforward steps make it effortless to interact with the application and perform face detection tasks effectively.

## Customization Options

The Face Detection App offers you the flexibility to customize various aspects, tailoring the application to your unique needs and preferences. Explore the following customization options:

**1. Model Customization:**
   - While this project employs a pre-trained Haar Cascade Classifier for face detection, you have the option to replace it with other models or detectors of your choice.
   - To do this, navigate to the `face_detector.py` module and make the necessary modifications within the `FaceDetector` class.
   - You can integrate different face detection models or detectors that align with your specific requirements.

**2. GUI Personalization:**
   - The graphical user interface (GUI) of the application can be customized to align with your aesthetic preferences and design vision.
   - Delve into the `faceDetection_gui.py` file, where you can make adjustments to elements such as colors, fonts, and widget sizes.
   - This level of customization empowers you to create a user interface that resonates with your unique design preferences, ensuring an engaging and user-friendly experience.

Feel free to explore the code and leverage these customization options. They provide you with the flexibility to adapt and enhance the application according to your specific objectives and preferences. Your creativity knows no bounds!

Enjoy utilizing the Face Detection App, and don't hesitate to reach out if you have questions, feedback, or suggestions. Your insights are highly valued!


