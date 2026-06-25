import os
import shutil
from fastapi import Depends

from auth.jwt import get_current_user
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form
)


from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.chroma import add_documents


from database.queries import save_document


from config.settings import settings



router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)




@router.post("/")
async def upload_pdf(

    file: UploadFile = File(...),

    user = Depends(
        get_current_user
    )

):

    # -------------------------
    # Save PDF temporarily
    # -------------------------


    file_path = os.path.join(
        settings.TEMP_STORAGE,
        file.filename
    )



    with open(
        file_path,
        "wb"
    ) as buffer:


        shutil.copyfileobj(
            file.file,
            buffer
        )



    # -------------------------
    # Load PDF
    # -------------------------


    documents = load_pdf(
        file_path
    )



    # -------------------------
    # Split chunks
    # -------------------------


    chunks = split_documents(
        documents
    )



    # -------------------------
    # Store vectors
    # -------------------------


    add_documents(
        chunks
    )



    # -------------------------
    # Save metadata
    # -------------------------


    save_document(

    user_id=user["id"],

    file_name=file.filename,

    file_url=file_path

)



    return {

        "message":
        "PDF uploaded successfully",


        "chunks":
        len(chunks)

    }