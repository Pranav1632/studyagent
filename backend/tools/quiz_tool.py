from langchain_core.tools import tool

from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import settings



llm = ChatGoogleGenerativeAI(
    model=settings.GEMINI_MODEL,
    google_api_key=settings.GOOGLE_API_KEY
)




@tool
def quiz_tool(
    topic: str
) -> str:

    """
    Generate MCQ quiz questions
    for given topic.
    """


    prompt = f"""

Create 5 multiple choice questions.

Topic:
{topic}


Format:

Question:

A)
B)
C)
D)

Answer:

Explanation:

"""


    response = llm.invoke(
        prompt
    )


    return response.content