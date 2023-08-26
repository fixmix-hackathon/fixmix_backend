from cl.message import message

SYSTEM_PROMPT = "You are a helpful assistant. Please answer in Japanese."

class chat:
    def __init__(self, user_id: str, chat_id: int, messages: list[message]):
        self.user_id = user_id
        self.chat_id = chat_id
        self.messages = messages

    def get_api_content(self, role_check: bool = True, show_system_prompt: bool = True) -> list[dict]:
        result = [{"role": "system", "content": SYSTEM_PROMPT}]
        for mes in sorted(self.messages):
            result.append({
                "role": mes.author,
                "content": mes.message
            })

        if not show_system_prompt:
            result = [i for i in result if i["role"] != "system"]

        if len(result) != 0:
            if role_check and result[-1]["role"] == "assistant":
                raise RuntimeError("Last Content's author is ASSISTANT.")
        else:
            raise RuntimeError("Zero Content's ChatCompletion is unavailable.")
        return result
