from fastapi import APIRouter


from pydantic import BaseModel


from langchain_core.messages import HumanMessage


from agents.study_agent import study_agent


from database.queries import save_message
from fastapi import Depends

from auth.jwt import get_current_user


router = APIRouter(

    prefix="/chat",

    tags=["Chat"]

)



# -----------------------------
# Request Schema
# -----------------------------

class ChatRequest(BaseModel):

    message: str





@router.post("/")
def chat(

    request: ChatRequest,

    user = Depends(
        get_current_user
    )

):


    # save user msg

    save_message(

        user["id"],

        "user",

        request.message

    )



    response = study_agent.invoke(

        {

            "messages":[

                HumanMessage(

                    content=request.message

                )

            ],


            "user_id":

            user["id"]

        }

    )




    answer = (

        response["messages"][-1]
        .content

    )



    # save AI response

    save_message(

       user["id"],

        "assistant",

        answer

    )




    return {

        "answer": answer

    }