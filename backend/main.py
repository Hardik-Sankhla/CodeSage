from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI(title="Code Review Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")

@app.post("/review/")
def review_code(code: str = Form(...)):
    prompt = (
        "You are a senior software engineer. Please review the following code, "
        "identify any bugs, suggest improvements, and optimization tips:\n\n"
        f"{code}"
    )
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": "deepseek-coder", "prompt": prompt, "stream": False},
            timeout=60
        )
        result = response.json()
        return {"review": result.get("response", "").strip()}
    except Exception as e:
        return {"error": str(e)}