import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.models import Model


class FeatureExtractor:
    def __init__(self):
        self.model = self._load_model()

    def _preprocess_image(self, image_path):
        img = load_img(image_path, target_size=(299, 299))
        img = img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = tf.keras.applications.inception_v3.preprocess_input(img)
        return img

    def _load_model(self):
        inception_v3_model = InceptionV3(input_shape=(299, 299, 3))
        inception_v3_model.layers.pop()
        inception_v3_model = Model(
            inputs=inception_v3_model.inputs,
            outputs=inception_v3_model.layers[-2].output,
        )
        return inception_v3_model

    def extract_image_features(self, image_path):
        img = self._preprocess_image(image_path)
        features = self.model.predict(img, verbose=0)
        return features
