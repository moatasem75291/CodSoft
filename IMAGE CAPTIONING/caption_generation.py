import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf


class CaptionGenerator:
    def __init__(self, model_path, tokenizer, max_caption_length):
        self.model = self._load_model(model_path)
        self.tokenizer = tokenizer
        self.max_caption_length = max_caption_length

    def _load_model(self, model_path):
        model = tf.keras.models.load_model(model_path)
        return model

    def generate_caption(self, image_features):
        in_text = "start "
        for _ in range(self.max_caption_length):
            sequence = self.tokenizer.texts_to_sequences([in_text])[0]
            sequence = pad_sequences([sequence], maxlen=self.max_caption_length)
            prediction = self.model.predict([image_features, sequence], verbose=0)
            idx = np.argmax(prediction)
            word = self.tokenizer.index_word[idx]
            in_text += " " + word
            if word == "end":
                break
        return in_text
