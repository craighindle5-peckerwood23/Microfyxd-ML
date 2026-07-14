class AudioIngestor:
    def __init__(self, name: str = "audio"):
        self.name = name

    def ingest(self, audio_bytes):
        # TODO: implement audio ingestion
        return {"raw_audio": audio_bytes}
