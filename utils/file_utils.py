from pathlib import Path
from datetime import datetime
import json


def ensure_output_dir(output_dir: str) -> Path:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def generate_filename(prefix: str = "result", ext: str = ".json") -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}{ext}"


def save_json(data: dict, output_dir: str, filename: str) -> str:
    path = ensure_output_dir(output_dir) / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return str(path)


def save_image(image_bytes: bytes, output_dir: str, filename: str) -> str:
    path = ensure_output_dir(output_dir) / filename
    with open(path, "wb") as f:
        f.write(image_bytes)
    return str(path)
