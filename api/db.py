from typing import Literal

import supabase
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cl.chat import chat
from cl.message import message

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase_client = supabase.create_client(url, key)


def getchat(user_id: str, chat_id: int) -> chat:
    # get messages from supabase.
    result = supabase_client.table("messages").select("*").eq("user_id", user_id).eq("chat_id", chat_id).execute()
    messages = [message(i["user_id"], i["chat_id"], i["message_id"], i["message"], i["author"],i["time"]) for i in result.data]
    return chat(user_id, chat_id, messages)

def getuserschatid(user_id: str) -> list[int]:
    result = supabase_client.table("chats").select("chat_id").eq("user_id", user_id).execute()
    return [i["chat_id"] for i in result.data]

def newchat(user_id: str) -> int:
    result = supabase_client.table("chats").insert({"user_id": user_id}).execute()
    return result.data[0]["chat_id"]


def addmessage(user_id: str, chat_id: int, newmessage: str, author: Literal["assistant", "user"]) -> message:
    # add message to supabase.
    res = supabase_client.table("messages").insert(
        {"user_id": user_id, "chat_id": chat_id, "message": newmessage, "author": author}).execute()
    given_message_id = res.data[0]["message_id"]
    given_time = res.data[0]["time"]
    return message(user_id, chat_id, given_message_id, newmessage, author,given_time)
