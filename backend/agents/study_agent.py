from langchain_google_genai import ChatGoogleGenerativeAI


from langgraph.graph import (
    StateGraph,
    START,
    END
)


from langgraph.prebuilt import (
    ToolNode,
    tools_condition
)


from config.settings import settings


from agents.state import AgentState


from tools.pdf_tool import pdf_search_tool
from tools.quiz_tool import quiz_tool
from tools.memory_tool import memory_tool



# ============================
# Gemini Model
# ============================


llm = ChatGoogleGenerativeAI(

    model=settings.GEMINI_MODEL,

    google_api_key=settings.GOOGLE_API_KEY

)



# ============================
# Register Tools
# ============================


tools = [

    pdf_search_tool,

    quiz_tool,

    memory_tool

]


llm_with_tools = (
    llm.bind_tools(
        tools
    )
)



# ============================
# Agent Node
# ============================


def agent_node(
    state: AgentState
):


    response = (
        llm_with_tools
        .invoke(
            state["messages"]
        )
    )


    return {

        "messages":[
            response
        ]

    }




# ============================
# Build Graph
# ============================


graph = StateGraph(
    AgentState
)



graph.add_node(
    "agent",
    agent_node
)



graph.add_node(
    "tools",
    ToolNode(
        tools
    )
)



graph.add_edge(
    START,
    "agent"
)



graph.add_conditional_edges(

    "agent",

    tools_condition

)



graph.add_edge(

    "tools",

    "agent"

)



study_agent = graph.compile()