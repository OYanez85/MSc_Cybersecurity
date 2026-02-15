from __future__ import annotations
from typing import Dict, Any

class ToolRuntime:
    """
    Herramientas simuladas para el experimento (sin efectos reales).
    """

    def send_email(self, to: str, body: str) -> Dict[str, Any]:
        return {"status": "sent(simulated)", "to": to, "bytes": len(body.encode("utf-8"))}

    def db_query(self, query: str) -> Dict[str, Any]:
        return {
            "status": "ok(simulated)",
            "rows": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}],
            "query": query
        }

    def http_get(self, url: str) -> Dict[str, Any]:
        return {"status": "ok(simulated)", "url": url, "code": 200, "body_preview": "<html>...</html>"}
