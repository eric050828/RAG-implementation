import os
import json

SESSION_CONTENT = {
    "chats": {
        "Chat1": {
            "path": "",
            "messages": []
        }
    }
}

SESSION_PATH = os.path.join("data", "session.json")

def _session_file_exists():
    if not os.path.exists(SESSION_PATH):
        with open(SESSION_PATH, "w") as file:
            json.dump(SESSION_CONTENT, file)

def save_session(data: dict) -> None:
    with open(SESSION_PATH, "w") as file:
        json.dump(data, file)

def load_session() -> dict:
    _session_file_exists()
    with open(SESSION_PATH, "r") as file:
        return json.load(file)

def create_empty_chat(title: str) -> dict:
    chat = {
        title: {
            "path": "",
            "messages": []
        }
    }
    return chat
