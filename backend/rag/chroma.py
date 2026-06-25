from langchain_chroma import Chroma

from config.settings import settings

from rag.embeddings import get_embeddings



def get_vector_store():


    vector_store = Chroma(
        persist_directory=settings.CHROMA_PATH,
        embedding_function=get_embeddings()
    )


    return vector_store




def add_documents(
    documents
):


    vector_store = get_vector_store()


    vector_store.add_documents(
        documents
    )


    return True