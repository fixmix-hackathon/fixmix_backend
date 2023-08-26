from flask import Flask, request
import openai

from api import db, ai

app = Flask(__name__)

MODEL = "gpt-3.5-turbo"
SYSTEM_PROMPT = "You are a helpful assistant. Please answer in Japanese."

@app.route("/call",methods=["POST"])
def callback_callmessage():
    """
    {
        "user_id": <UID>,
        "chat_id": <INT>,
        "content": <TEXT>
    }
    """
    uid: str = request.json["user_id"]
    chat_id: int = int(request.json["chat_id"])
    content: str = request.json["content"]

    # get chat history
    chat = db.getchat(uid, chat_id)

    # send add message query to db
    new_message = db.addmessage(uid, chat_id, content, "user")

    # new message append to chat(variable)
    chat.messages.append(new_message)

    reply = ai.run(chat)

    # send add reply query to db
    reply_message = db.addmessage(uid, chat_id, reply, "assistant")

    chat.messages.append(reply_message)
    return chat.get_content()


@app.route("/",methods=["GET"])
def callback_route_get():
    return "THIS IS GET TEST 0825."
