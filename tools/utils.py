import os
import json
import uuid
from datetime import datetime


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def generate_id():
    return str(uuid.uuid4())


def timestamp():
    return datetime.utcnow().isoformat()


def save_json(data, path):
    ensure_dir(os.path.dirname(path))

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
