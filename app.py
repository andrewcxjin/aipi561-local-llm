from fastapi import FastAPI
from pydantic import BaseModel
from llm_wrapper import ask_llm

app = FastAPI(title="Local LLM API", version="1.0")

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "Welcome to the Local LLM API!"}

@app.post("/ask")
def ask(req: PromptRequest):
    response = ask_llm(req.prompt)
    return {"response": response}