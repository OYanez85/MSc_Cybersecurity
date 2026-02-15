from __future__ import annotations
import re
from typing import Tuple

INSTRUCTION_PATTERNS = [
    r"\bignore (all|previous) instructions\b",
    r"\byou are now\b",
    r"\bdo not follow\b",
    r"\bcall (the )?tool\b",
    r"\bsend_email\b",
    r"\bdb_query\b",
    r"\bhttp_get\b",
    r"\bdebug mode\b",
]

def sanitize_retrieved_text(text: str) -> Tuple[str, int]:
    """
    Convierte texto recuperado (RAG) en 'datos' neutralizando patrones
    típicos de instrucciones maliciosas.
    """
    hits = 0
    out = text
    for pat in INSTRUCTION_PATTERNS:
        if re.search(pat, out, flags=re.IGNORECASE):
            hits += 1
            out = re.sub(pat, "[REDACTED_INSTRUCTION]", out, flags=re.IGNORECASE)
    out = re.sub(
        r"^\s*(step|paso)\s*\d+[:\-].*$",
        "[REDACTED_STEP_LINE]",
        out,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    return out, hits
