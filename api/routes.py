from api.ingest import ingest_text


def predict_from_text(text: str) -> dict:
    return ingest_text(text)
