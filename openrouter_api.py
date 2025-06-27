import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
REFERER = os.getenv("SITE_URL", "")
TITLE = os.getenv("SITE_NAME", "")

def chat_with_openrouter(messages, model="deepseek/deepseek-chat:free"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": REFERER,
        "X-Title": TITLE
    }
    payload = {
        "model": model,
        "messages": messages[-20:]  # keep last 20 turns (adjust if needed)
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload))
    if response.ok:
        return response.json()["choices"][0]["message"]["content"]
    return f"[Error] {response.status_code}: {response.text}"

def summarize(text, memory=None):
    """Summarize with optional conversational memory."""
    system_prompt = {"role": "system", "content": "You are a helpful research assistant who summarizes content clearly."}
    base = [system_prompt]
    if memory:
        base += memory
    base.append({"role": "user", "content": f"Summarize this:\n{text[:4000]}"})
    return chat_with_openrouter(base)
