from repositories.knowledge_repository import KnowledgeRepository

from services.metadata_service import MetadataService
from services.ingestion_service import IngestionService

from clients.vector_client import VectorClient
from clients.rag_client import RAGClient


class KnowledgeService:

    def __init__(self):

        self.repository = KnowledgeRepository()

        self.metadata = MetadataService()

        self.ingestion = IngestionService()

        self.vector = VectorClient()

        self.rag = RAGClient()

    def overview(self):

        return {

            "collections": self.repository.collections(),

            "metadata": self.metadata.summary(),

            "ingestion": self.ingestion.status(),

            "vector": self.vector.status(),

            "rag": self.rag.status()

        }
