import re
from tensorflow.keras.preprocessing.text import Tokenizer


class PreparedCaptions:
    def __init__(self, file_path):
        self.file_path = file_path

    def _load_captions(self):
        with open(self.file_path, "r") as f:
            captions = f.readlines()
            captions = [caption.lower() for caption in captions]
        return captions

    def _clean_text(self, text):
        text = re.sub(r"[^\w\s]", "", text)
        text = re.sub(r"\d+", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def tokenize_captions(self):
        captions = self._load_captions()
        captions = [self._clean_text(caption.split(",")[1]) for caption in captions]
        max_caption_length = max(len(caption.split()) for caption in captions) + 1
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(captions)
        return tokenizer, max_caption_length
