from fastapi import FastAPI
from pydantic import BaseModel

from ai_agent import get_response_from_ai_agent

app = FastAPI(
    title="LangGraph Chatbot"
)


class RequestState(BaseModel):

    model_name: str
    model_provider: str
    message: str
    allow_search: bool
    thread_id: str


ALLOWED_MODELS = [

    "llama-3.3-70b-versatile",
    "gemini-2.5-flash"
]

@app.get("/")
def show():
    print("successfully connected to the backend!")

@app.post("/chat")
def chat(request: RequestState):
    """
    Choose the correct tool when user ask something.
    """
    if request.model_name not in ALLOWED_MODELS:

        return {
            "error":
            "Invalid Model"
        }

    response = get_response_from_ai_agent(
        model_name=request.model_name,
        provider=request.model_provider,
        query=request.message,
        allow_search=request.allow_search,
        thread_id=request.thread_id
    )

    return {
        "response": response
    }


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=9999
    )