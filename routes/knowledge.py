from fastapi import APIRouter

from services.knowledge_service import KnowledgeService

router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge"]
)

service = KnowledgeService()


@router.get("/")
def knowledge():

    return service.overview()
