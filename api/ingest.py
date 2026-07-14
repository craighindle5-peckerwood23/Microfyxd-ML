from typing import Dict

def ingest_payload(raw: Dict[str, any]) -> Dict[str, any]:
    return {
        "text": raw.get("text", ""),
        "meta": raw.get("meta", {}),
    }
