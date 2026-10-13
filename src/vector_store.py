from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os


class VectorStore:
    def __init__(self, _chunks=None):
        # 1. Load a pretrained Sentence Transformer model
        self.model = SentenceTransformer(os.getenv("EMBEDDING_MODEL"))
        self.index = None
        self.chunks = _chunks


    def  encode(self):

        # The sentences to encode
        # sentences = [
        #     "The weather is lovely today.",
        #     "It's so sunny outside!",
        #     "He drove to the stadium.",
        # ]

        # 2. Calculate embeddings by calling model.encode()
        embeddings = self.model.encode(self.chunks)
        # [3, 384]

        # 3. Calculate the embedding similarities
        # similarities = self.model.similarity(embeddings, embeddings)
        # tensor([[1.0000, 0.6660, 0.1046],
        #         [0.6660, 1.0000, 0.1411],
        #         [0.1046, 0.1411, 1.0000]])

        # Get embedding dimension
        dimension = embeddings.shape[1]

        # Create a flat index using L2 distance
        self.index = faiss.IndexFlatL2(dimension)

        # Add embeddings to the index
        self.index.add(np.array(embeddings))


    def  search(self, query, top_k=5):

        query_embedding = self.model.encode([query])

        # Vector search
        distances, indices = self.index.search(query_embedding, top_k)

        results = []

        for i in indices[0]:
            results.append(self.chunks[i])

        return "\n\n".join(results)