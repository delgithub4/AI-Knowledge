from fastapi import FastAPI

from routes.knowledge import router as knowledge_router
from routes.health import router as health_router

app = FastAPI(
    title="AI-Knowledge",
    version="1.0.0"
)

app.include_router(knowledge_router)
app.include_router(health_router)


@app.get("/")
def home():

    return {

        "service":"AI-Knowledge",

        "status":"running"

    }
