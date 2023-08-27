from typing import Literal

AUTHORS = Literal["assistant", "user", "system"]

class message:
    def __init__(self, user_id: str, chat_id: int, message_id: str, message: str, author: AUTHORS, send_time: str):
        self.user_id = user_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.message = message
        self.author = author
        self.send_time = send_time

    def __lt__(self, other):
        # sorting用
        return self.message_id < other.message_id