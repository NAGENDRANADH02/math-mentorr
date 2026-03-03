from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL
import numpy as np

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(EMBED_MODEL)

    def embed(self, texts):
        return self.model.encode(texts)