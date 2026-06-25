from langchain_core.tools import tool

from rag.retriever import retrieve_documents



@tool
def pdf_search_tool(
    question: str
) -> str:
    """
    Search uploaded PDF documents
    and return relevant context.
    """


    docs = retrieve_documents(
        question
    )


    if not docs:
        return "No relevant PDF content found."


    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )


    return context