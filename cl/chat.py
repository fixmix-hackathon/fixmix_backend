from message import message

class chat:
    def __init__(self, user_id: str, chat_id: int, messages: list[message]):
        self.user_id = user_id
        self.chat_id = chat_id
        self.messages = messages

    def get_api_content(self) -> list[dict]:
        result = []
        for mes in sorted(self.messages):
            result.append({
                "role": mes.author,
                "content": mes.message
            })
        if len(result) != 0:
            if result[-1]["role"] == "assistant":
                raise RuntimeError("Last Content's author is ASSISTANT.")
        else:
            raise RuntimeError("Zero Content's ChatCompletion is unavailable.")
        return result
