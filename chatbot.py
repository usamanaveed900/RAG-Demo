class RAGChatbot:
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator

    def get_response(self, query):
        """Retrieve context and generate a response."""
        retrieved_docs = self.retriever.retrieve(query)
        response = self.generator.generate_response(query, retrieved_docs)
        return response
