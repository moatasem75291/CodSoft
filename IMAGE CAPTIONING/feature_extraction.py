import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
import numpy as np

# Load pre-trained VGG model without top classification layers
base_model = VGG16(weights='imagenet', include_top=False)

# Create a new model that takes image input and outputs features from a specific layer
image_input = tf.keras.layers.Input(shape=(224, 224, 3))
vgg_features = base_model(image_input)
vgg_features = tf.keras.layers.Flatten()(vgg_features)
image_model = Model(inputs=image_input, outputs=vgg_features)

# Example function for feature extraction from an image
def extract_features(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = tf.keras.applications.vgg16.preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    features = image_model.predict(img)
    return features

# Example usage for feature extraction
image_path = 'path_to_your_image.jpg'
features = extract_features(image_path)
print(features)
