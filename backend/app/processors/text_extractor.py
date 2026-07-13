from pathlib import Path

from docx import Document
from pypdf import PdfReader


class TextExtractor:

    @staticmethod
    def extract(file_path: str) -> str:

        suffix = Path(file_path).suffix.lower()

        if suffix == ".txt":
            return TextExtractor._extract_txt(file_path)

        if suffix == ".pdf":
            return TextExtractor._extract_pdf(file_path)

        if suffix == ".docx":
            return TextExtractor._extract_docx(file_path)

        raise ValueError("Unsupported file type")

    @staticmethod
    def _extract_txt(file_path: str) -> str:

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as file:

            return file.read()

    @staticmethod
    def _extract_pdf(file_path: str) -> str:

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    @staticmethod
    def _extract_docx(file_path: str) -> str:

        document = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )