import faiss
import numpy as np

class Retriever:
    def __init__(self, embeddings, documents):
        self.documents = documents
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings))

    def search(self, query_embedding, top_k=3):
        D, I = self.index.search(query_embedding, top_k)
        results = []
        for idx, dist in zip(I[0], D[0]):
            results.append({
                "source": self.documents[idx]["source"],
                "content": self.documents[idx]["content"],
                "score": float(1/(1+dist))
            })
        return results