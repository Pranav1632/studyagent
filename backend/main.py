from fastapi import FastAPI


from routes.upload import router as upload_router
from routes.chat import router as chat_router



app = FastAPI(

    title="AI Study Assistant Agent",

    description="""

    Agentic AI Study Assistant
    
    Features:
    
    - PDF Chat
    - RAG
    - LangGraph Agent
    - Tool Calling
    - Memory
    - Quiz Generator

    """,

    version="1.0.0"

)



# -----------------------------
# Routes
# -----------------------------


app.include_router(
    upload_router
)


app.include_router(
    chat_router
)



# -----------------------------
# Health Check
# -----------------------------


@app.get("/")
def home():


    return {

        "status": "running",

        "message":
        "AI Study Assistant Backend"

    }