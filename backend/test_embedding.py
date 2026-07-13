from app.ai.embedding_service import EmbeddingService

service = EmbeddingService()

text = """
Enterprise Intelligence OS uses AI,
RAG, PostgreSQL,
FastAPI,
Docker
and Multi-Agent Systems.
"""

embedding = service.generate_embedding(text)

print(f"Vector Length: {len(embedding)}")

print()

print(embedding[:20])