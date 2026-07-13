from sqlalchemy.orm import Session

from app.ai.embedding_service import EmbeddingService
from app.processors.text_chunker import TextChunker
from app.processors.text_extractor import TextExtractor


class DocumentProcessingTask:

    def __init__(self):
        self.extractor = TextExtractor()
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()

    def process_document(
        self,
        db: Session,
        document,
    ):
        """
        Complete AI processing pipeline.

        This method will later:

        1. Extract text
        2. Chunk text
        3. Generate embeddings
        4. Store embeddings in PostgreSQL
        """

        text = self.extractor.extract(
            document.file_path
        )

        chunks = self.chunker.chunk(
            text
        )

        embeddings = self.embedding_service.generate_embeddings(
            chunks
        )

        print(
            f"Generated {len(embeddings)} embeddings "
            f"for document {document.id}"
        )

        # Sprint 6.6:
        # Save embeddings to PostgreSQL