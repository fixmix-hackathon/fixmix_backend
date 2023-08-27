import os

from models.message import message

class chat:
    def __init__(self, user_id: str, chat_id: int, messages: list[message]):
        self.user_id = user_id
        self.chat_id = chat_id
        self.messages = messages

    def get_api_content(self) -> list[dict]:
        return self._jsonalize(role_check=True, show_system_prompt=True, show_timestamp=False)

    def get_content(self) -> list[dict]:
        return self._jsonalize(role_check=False, show_system_prompt=False, show_timestamp=True)

    def _jsonalize(self, role_check: bool, show_system_prompt: bool, show_timestamp: bool) -> list[dict]:
        result = [{"role": "system", "content": os.getenv("SYSTEM_PROMPT")}]
        for mes in sorted(self.messages):
            _json = {"role": mes.author, "content": mes.message}
            if show_timestamp:
                _json["time"] = mes.send_time
            result.append(_json)

        if not show_system_prompt:
            result = [i for i in result if i["role"] != "system"]

        if len(result) != 0:
            if role_check and result[-1]["role"] == "assistant":
                raise RuntimeError("Last Content's author is ASSISTANT.")
        else:
            raise RuntimeError("Zero Content's ChatCompletion is unavailable.")
        return result
