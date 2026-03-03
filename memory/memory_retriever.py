from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL, SIMILARITY_THRESHOLD
import numpy as np

model = SentenceTransformer(EMBED_MODEL)

def search_similar(problem, past_data):
    if not past_data:
        return None

    past_texts = [p[0] for p in past_data]
    past_solutions = [p[1] for p in past_data]

    emb_current = model.encode([problem])
    emb_past = model.encode(past_texts)

    similarities = np.dot(emb_current, emb_past.T)[0]
    best_idx = np.argmax(similarities)

    if similarities[best_idx] > SIMILARITY_THRESHOLD:
        return {
            "similarity": float(similarities[best_idx]),
            "solution": past_solutions[best_idx]
        }
    return None