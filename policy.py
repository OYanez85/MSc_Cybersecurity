from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Tuple
import re

SENSITIVE_KEYS = {"api_key", "system_prompt", "secret", "password", "token"}

@dataclass(frozen=True)
class Decision:
    allowed: bool
    reason: str

class PolicyEngine:
    """
    Motor determinista: valida tool calls antes de ejecutar.
    Reglas simples, auditables y reproducibles.
    """

    def __init__(self, allowed_email_domains: Tuple[str, ...] = ("axa.com", "example.com")):
        self.allowed_email_domains = allowed_email_domains

    def _contains_sensitive_exfil(self, payload: str) -> bool:
        payload_l = payload.lower()
        return any(k in payload_l for k in SENSITIVE_KEYS)

    def _domain_ok(self, email: str) -> bool:
        email = email.strip().lower()
        if "@" not in email:
            return False
        domain = email.split("@", 1)[1]
        return any(domain == d or domain.endswith("." + d) for d in self.allowed_email_domains)

    def validate_tool_call(self, tool: str, args: Dict[str, Any], context_meta: Dict[str, Any]) -> Decision:
        allowed_tools = {"send_email", "db_query", "http_get"}
        if tool not in allowed_tools:
            return Decision(False, f"Tool '{tool}' no permitida (deny-by-default).")

        blob = str(args)
        if self._contains_sensitive_exfil(blob):
            return Decision(False, "Bloqueado: posible exfiltración de información sensible.")

        if tool == "send_email":
            to = str(args.get("to", ""))
            if not self._domain_ok(to):
                return Decision(False, f"Bloqueado: dominio de email no permitido: {to}")

            body = str(args.get("body", ""))
            if re.search(r"\b(ignore|override|bypass|debug mode)\b", body, re.IGNORECASE):
                return Decision(False, "Bloqueado: contenido con patrón de bypass/override.")

        if tool == "db_query":
            q = str(args.get("query", "")).strip()
            if not q.lower().startswith("select"):
                return Decision(False, "Bloqueado: solo se permite SELECT en este prototipo.")
            if re.search(r"(--|;|\bor\b\s+1=1|\bdrop\b|\bunion\b)", q, re.IGNORECASE):
                return Decision(False, "Bloqueado: patrón típico de inyección SQL detectado.")

        if tool == "http_get":
            url = str(args.get("url", ""))
            if re.search(r"(localhost|127\.0\.0\.1|169\.254\.169\.254|10\.|192\.168\.|172\.(1[6-9]|2\d|3[0-1])\.)", url):
                return Decision(False, "Bloqueado: posible SSRF a red interna/metadata.")

        return Decision(True, "Permitido por política.")
