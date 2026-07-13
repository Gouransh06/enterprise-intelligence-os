import os
import shutil
import uuid

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.models.document import Document
from app.repositories.document_repository import DocumentRepository


class DocumentService:

    ALLOWED_TYPES = {
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain",
    }

    MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB

    UPLOAD_DIRECTORY = "uploads"

    def __init__(self):
        self.document_repository = DocumentRepository()

        os.makedirs(
            self.UPLOAD_DIRECTORY,
            exist_ok=True,
        )

    def upload_document(
        self,
        db: Session,
        file: UploadFile,
        owner_id: int,
    ) -> Document:

        if file.content_type not in self.ALLOWED_TYPES:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file type",
            )

        unique_filename = (
            f"{uuid.uuid4()}_{file.filename}"
        )

        file_path = os.path.join(
            self.UPLOAD_DIRECTORY,
            unique_filename,
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer,
            )

        file_size = os.path.getsize(file_path)

        if file_size > self.MAX_FILE_SIZE:
            os.remove(file_path)

            raise HTTPException(
                status_code=400,
                detail="File exceeds maximum size of 20 MB",
            )

        document = Document(
            filename=unique_filename,
            original_filename=file.filename,
            content_type=file.content_type,
            file_size=file_size,
            file_path=file_path,
            owner_id=owner_id,
        )

        return self.document_repository.create(
            db,
            document,
        )

    def get_documents(
        self,
        db: Session,
        owner_id: int,
    ):

        return self.document_repository.get_all_by_owner(
            db,
            owner_id,
        )

    def delete_document(
        self,
        db: Session,
        document_id: int,
        owner_id: int,
    ):

        document = self.document_repository.get_by_id(
            db,
            document_id,
        )

        if document is None:
            raise HTTPException(
                status_code=404,
                detail="Document not found",
            )

        if document.owner_id != owner_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied",
            )

        if os.path.exists(document.file_path):
            os.remove(document.file_path)

        self.document_repository.delete(
            db,
            document,
        )