import openai
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.chat import chat

openai.organization = os.getenv("env_openai_orgid")
openai.api_key = os.getenv("env_openai_apikey")


def run(send_chat: chat) -> str:
    # call OpenAI's ChatCompletion.
    cmpl = openai.ChatCompletion.create(
        model=os.getenv("openai_model"),
        messages=send_chat.get_api_content(),
        temperature=0
    )
    return cmpl["choices"][0]["message"]["content"]