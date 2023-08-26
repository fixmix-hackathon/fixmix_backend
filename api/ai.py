import openai
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cl.chat import chat

openai.organization = os.getenv("env_openai_orgid")
openai.api_key = os.getenv("env_openai_apikey")
MODEL = os.getenv("openai_model")


def run(send_chat: chat) -> str:
    global MODEL

    # call OpenAI's ChatCompletion.
    cmpl = openai.ChatCompletion.create(
        model=MODEL,
        messages=send_chat.get_api_content(),
        temperature=0
    )
    return cmpl["choices"][0]["message"]["content"]