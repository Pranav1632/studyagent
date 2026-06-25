from langchain_core.tools import tool

from database.queries import get_chat_history



@tool
def memory_tool(
    user_id: str
) -> str:


    """
    Fetch previous conversation
    history of user.
    """

    
    messages = get_chat_history(
        user_id
    )


    if not messages:

        return "No previous memory found."



    history = ""


    for msg in messages:

        history += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )


    return history