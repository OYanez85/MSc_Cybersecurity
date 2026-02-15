from __future__ import annotations
import json
from pathlib import Path

KB_PATH = Path(__file__).resolve().parent / "kb.jsonl"

def ingest_doc(doc_id: str, text: str) -> None:
    KB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with KB_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"doc_id": doc_id, "text": text}, ensure_ascii=False) + "\n")

def load_kb() -> list[dict]:
    if not KB_PATH.exists():
        return []
    return [json.loads(line) for line in KB_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
