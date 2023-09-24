# CodSoft Internship Project: Image Captioning App with PyQt5 GUI

This project is an Image Captioning Application created using Python, TensorFlow, and PyQt5. It allows users to upload images and automatically generates captions for them using a pre-trained model.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Customization](#customization)

## Overview

Our CodSoft internship project presents an Image Captioning Application featuring a user-friendly PyQt5-based graphical user interface (GUI). With this application, users can effortlessly upload images, and the application will promptly generate descriptive captions for the uploaded images.

## Getting Started

### Prerequisites

Before you start using this project, ensure you have the following installed:

- Python (3.7 or higher)
- TensorFlow
- Computer Vision
- NLP
- PyQt5

### Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/CodSoft.git
   cd CodSoft
   ```
## Project Structure

The project is organized as follows:

- **main.py**: This serves as the primary application script and is responsible for initializing the PyQt5 GUI and managing user interactions.

- **gui_app.py**: This script defines the PyQt5-based graphical user interface used for image uploading and caption generation.

- **feature_extraction.py**: In this module, you'll find functionality for extracting image features using a pre-trained model. (InceptionV3)

- **caption_generation.py**: This module provides functions for generating captions for images.

- **prepared_captions.py**: This component handles the loading and preprocessing of prepared captions from a text file.

- **README.md**: You're currently reading this documentation file (-_-), which provides an overview of the project, instructions, and information on its structure.

Feel free to explore each component to gain a deeper understanding of the project's organization and functionality.

## Usage

To make the most of the application, simply follow these straightforward steps:

1. **Launch the Application**: Start the application by running the following command in your terminal or command prompt:

    ```shell
    python main.py
    ```

    This command initializes the application.

2. **Explore the GUI**: Upon launch, the graphical user interface (GUI) will open. It prominently features an "Upload Image" button and an area dedicated to displaying captions.

3. **Upload an Image**: To generate a caption for an image, click the "Upload Image" button. This action will prompt you to select an image file from your computer.

4. **Caption Generation**: After selecting an image, the application will display the uploaded image within the GUI. It will then proceed to automatically generate a descriptive caption for the image.

5. **Caption Display**: The generated caption will be presented below the displayed image, allowing you to easily read and analyze the caption.

These steps make it easy to interact with the application and obtain image captions effortlessly.

Feel free to explore and enjoy the capabilities of the Image Captioning App with the PyQt5 GUI.

## Customization

The Image Captioning App offers you the flexibility to customize various aspects to tailor the application to your unique needs and preferences:

1. **Model Customization**: You have the option to replace the pre-trained model used for image captioning. This can be achieved by modifying the code in the `feature_extraction.py` file to include your own model or specifying a different model path within the `main.py` script.

2. **Caption Variability**: You can customize the captions used by modifying the caption file path within the `main.py` script. This allows you to work with different sets of captions to suit your specific use case.

3. **GUI Personalization**: The application's graphical user interface (GUI) can be customized to match your aesthetic preferences. Feel free to explore the `gui_app.py` file, where you can make changes to colors, fonts, and widget sizes. This empowers you to create a user interface that aligns with your design vision.

Don't hesitate to delve into the code and explore these customization options. They provide you with the flexibility to adapt and enhance the application to meet your specific requirements, ensuring it aligns perfectly with your objectives and preferences.

