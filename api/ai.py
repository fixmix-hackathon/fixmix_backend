import openai
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cl.chat import chat

openai.organization = os.getenv("env_openai_orgid")
openai.api_key = os.getenv("env_openai_apikey")
MODEL = "gpt-3.5-turbo"

SYSTEM_PROMPT = "You are a helpful assistant. Please answer in Japanese."


def run(send_chat: chat) -> str:
    # call OpenAI's ChatCompletion.
    send_chat = [{"role": "system", "content": SYSTEM_PROMPT}] + send_chat
    cmpl = openai.ChatCompletion.create(
        model=MODEL,
        messages=send_chat,
        temperature=0
    )
    return cmpl["choices"][0]["message"]["content"]