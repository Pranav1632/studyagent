from rag.chroma import get_vector_store



def retrieve_documents(
    query: str,
    k: int = 5
):


    vector_store = get_vector_store()


    results = (
        vector_store
        .similarity_search(
            query,
            k=k
        )
    )


    return results