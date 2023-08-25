from flask import Flask, request
import openai
import os

app = Flask(__name__)

openai.organization = os.getenv("env_openai_orgid")
openai.api_key = os.getenv("env_openai_apikey")
MODEL = "gpt-3.5-turbo"
SYSTEM_PROMPT = "You are a helpful assistant. Please answer in Japanese."

def run(content: str) -> str:
    # call OpenAI's ChatCompletion.
    cmpl = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": content}
        ],
        temperature=0
    )
    return cmpl["choices"][0]["message"]["content"]

@app.route('/', methods=["POST"])
def callback_post():
    # get user's prompt from frontend.
    content = request.json["content"]

    # call OpenAI API.
    result = run(content)
    return result

@app.route('/', methods=["GET"])
def callback_get():
    # debug
    return "THIS IS GET."

@app.route('/test', methods=["POST"])
def callback_post_test():
    # debug
    content = request.json["content"]
    return content