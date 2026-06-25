from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config.settings import settings



def get_embeddings():

    embeddings = GoogleGenerativeAIEmbeddings(
        model=settings.EMBEDDING_MODEL,
        google_api_key=settings.GOOGLE_API_KEY
    )


    return embeddings