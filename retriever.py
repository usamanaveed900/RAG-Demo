import faiss
import numpy as np

class Retriever:
    def __init__(self, documents):
        self.documents = documents
        self.index = None
        self.embeddings = None
        self.build_index()

    def build_index(self):
        """Create FAISS index for document embeddings."""
        self.embeddings = [np.random.rand(768).astype("float32") for _ in self.documents]
        self.index = faiss.IndexFlatL2(768)
        self.index.add(np.array(self.embeddings))

    def retrieve(self, query):
        """Retrieve the top documents based on similarity."""
        query_embedding = np.random.rand(768).astype("float32")  # Mock query embedding
        _, top_indices = self.index.search(query_embedding.reshape(1, -1), k=2)
        return [self.documents[i] for i in top_indices[0]]
