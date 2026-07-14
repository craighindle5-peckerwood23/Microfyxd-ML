#!/usr/bin/env bash

set -e

# Create directories
mkdir -p api
mkdir -p ingestion
mkdir -p normalization
mkdir -p feature_extraction
mkdir -p models
mkdir -p structured_engine
mkdir -p post_processing
mkdir -p orchestration
mkdir -p utils

# README
cat > README.md << 'EOF'
# Microfyxd-ML

A simple modular ML pipeline demo:
ingestion -> normalization -> feature_extraction -> models -> structured_engine -> post_processing -> orchestration -> api.
EOF

# main.py
cat > main.py << 'EOF'
from api.predict import run_prediction_demo


def run_example() -> None:
    print("=== Microfyxd-ML Demo ===")
    run_prediction_demo()


if __name__ == "__main__":
    run_example()
EOF

# api/ingest.py
cat > api/ingest.py << 'EOF'
from orchestration.pipeline import Pipeline
from utils.logging import get_logger

logger = get_logger(__name__)


def ingest_text(text: str) -> dict:
    logger.info("API ingest_text called")
    pipeline = Pipeline()
    result = pipeline.run({"text": text})
    return result
EOF

# api/predict.py
cat > api/predict.py << 'EOF'
from api.ingest import ingest_text
from utils.logging import get_logger

logger = get_logger(__name__)


def run_prediction_demo() -> None:
    sample_text = "Hello world, this is a Microfyxd-ML demo message."
    logger.info("Running prediction demo")
    result = ingest_text(sample_text)
    print("Final result:")
    print(result)
EOF

# api/routes.py
cat > api/routes.py << 'EOF'
from api.ingest import ingest_text


def predict_from_text(text: str) -> dict:
    return ingest_text(text)
EOF

# ingestion/audio_ingest.py
cat > ingestion/audio_ingest.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


class AudioIngestor:
    def __init__(self, name: str = "audio"):
        self.name = name

    def ingest(self, audio_bytes: bytes) -> dict:
        logger.info("Ingesting audio bytes")
        return {"audio": audio_bytes, "source": self.name}
EOF

# ingestion/email_ingest.py
cat > ingestion/email_ingest.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


class EmailIngestor:
    def __init__(self, name: str = "email"):
        self.name = name

    def ingest(self, subject: str, body: str) -> dict:
        logger.info("Ingesting email")
        return {"subject": subject, "body": body, "source": self.name}
EOF

# ingestion/ocr_ingest.py
cat > ingestion/ocr_ingest.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


class OCRIngestor:
    def __init__(self, name: str = "ocr"):
        self.name = name

    def ingest(self, image_bytes: bytes) -> dict:
        logger.info("Ingesting OCR image bytes")
        return {"image": image_bytes, "source": self.name}
EOF

# ingestion/text_ingest.py
cat > ingestion/text_ingest.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


class TextIngestor:
    def __init__(self, name: str = "text"):
        self.name = name

    def ingest(self, text: str) -> dict:
        logger.info("Ingesting text")
        return {"text": text, "source": self.name}
EOF

# normalization/cleaner.py
cat > normalization/cleaner.py << 'EOF'
import re
from utils.logging import get_logger

logger = get_logger(__name__)


def clean_text(text: str) -> str:
    logger.info("Cleaning text")
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
EOF

# normalization/segmented.py
cat > normalization/segmented.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


def segment_text(text: str) -> list:
    logger.info("Segmenting text into sentences (simple split)")
    return [text]
EOF

# normalization/tokenizer.py
cat > normalization/tokenizer.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


def tokenize(text: str) -> list:
    logger.info("Tokenizing text")
    return text.split()
EOF

# feature_extraction/vectorizer.py
cat > feature_extraction/vectorizer.py << 'EOF'
from collections import Counter
from utils.logging import get_logger

logger = get_logger(__name__)


def bow_vector(tokens: list) -> dict:
    logger.info("Creating bag-of-words vector")
    return dict(Counter(tokens))
EOF

# feature_extraction/embeddings.py
cat > feature_extraction/embeddings.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


def dummy_embeddings(tokens: list) -> dict:
    logger.info("Creating dummy embeddings")
    return {token: float(len(token)) for token in tokens}
EOF

# feature_extraction/stats_features.py
cat > feature_extraction/stats_features.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


def stats_features(tokens: list) -> dict:
    logger.info("Computing simple stats features")
    length = len(tokens)
    avg_len = sum(len(t) for t in tokens) / length if length > 0 else 0.0
    return {"token_count": length, "avg_token_length": avg_len}
EOF

# models/registry.py
cat > models/registry.py << 'EOF'
from typing import Dict, Any
from utils.logging import get_logger

logger = get_logger(__name__)


class ModelRegistry:
    def __init__(self):
        self._models: Dict[str, Any] = {}

    def register(self, name: str, model: Any) -> None:
        logger.info(f"Registering model: {name}")
        self._models[name] = model

    def get(self, name: str) -> Any:
        logger.info(f"Fetching model: {name}")
        return self._models.get(name)
EOF

# models/loader.py
cat > models/loader.py << 'EOF'
from models.registry import ModelRegistry
from models.classifier import RuleBasedClassifier
from utils.logging import get_logger

logger = get_logger(__name__)


def load_models() -> ModelRegistry:
    logger.info("Loading models into registry")
    registry = ModelRegistry()
    registry.register("rule_classifier", RuleBasedClassifier())
    return registry
EOF

# models/classifier.py
cat > models/classifier.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


class RuleBasedClassifier:
    def predict(self, features: dict) -> dict:
        logger.info("Running rule-based classifier")
        token_count = features.get("stats", {}).get("token_count", 0)
        if token_count == 0:
            label = "empty"
        elif token_count < 5:
            label = "short"
        else:
            label = "long"
        return {"label": label}
EOF

# models/scorer.py
cat > models/scorer.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


def score_prediction(prediction: dict) -> dict:
    logger.info("Scoring prediction")
    label = prediction.get("label", "unknown")
    confidence = 0.5
    if label == "empty":
        confidence = 0.9
    elif label == "short":
        confidence = 0.7
    elif label == "long":
        confidence = 0.8
    return {"label": label, "confidence": confidence}
EOF

# structured_engine/engine_parts.py
cat > structured_engine/engine_parts.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


class EnginePart:
    def __init__(self, name: str):
        self.name = name

    def process(self, data: dict) -> dict:
        logger.info(f"EnginePart {self.name} processing data")
        return data
EOF

# structured_engine/hunter.py
cat > structured_engine/hunter.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


class Hunter:
    def __init__(self, name: str = "default_hunter"):
        self.name = name

    def hunt(self, data: dict) -> dict:
        logger.info("Hunter routing data")
        data["route"] = "default"
        return data
EOF

# structured_engine/intent_classifier.py
cat > structured_engine/intent_classifier.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


class IntentClassifier:
    def classify_intent(self, text: str) -> str:
        logger.info("Classifying intent (dummy)")
        if "hello" in text.lower():
            return "greeting"
        return "generic"
EOF

# post_processing/confidence.py
cat > post_processing/confidence.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


def adjust_confidence(conf: float, intent: str) -> float:
    logger.info("Adjusting confidence based on intent")
    if intent == "greeting":
        return min(1.0, conf + 0.1)
    return conf
EOF

# post_processing/output_normalizer.py
cat > post_processing/output_normalizer.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


def normalize_output(prediction: dict) -> dict:
    logger.info("Normalizing output")
    return {
        "prediction": prediction.get("label"),
        "confidence": prediction.get("confidence"),
    }
EOF

# post_processing/result_mapper.py
cat > post_processing/result_mapper.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


def map_result(normalized: dict, intent: str) -> dict:
    logger.info("Mapping result to final structure")
    return {
        "intent": intent,
        "prediction": normalized.get("prediction"),
        "confidence": normalized.get("confidence"),
    }
EOF

# orchestration/state_tracker.py
cat > orchestration/state_tracker.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


class StateTracker:
    def __init__(self):
        self.states = []

    def log_state(self, stage: str, data: dict) -> None:
        logger.info(f"StateTracker logging stage: {stage}")
        self.states.append((stage, data))
EOF

# orchestration/job_manager.py
cat > orchestration/job_manager.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


class JobManager:
    def __init__(self):
        self.jobs = []

    def submit(self, job_data: dict) -> None:
        logger.info("JobManager submitting job")
        self.jobs.append(job_data)

    def list_jobs(self) -> list:
        return self.jobs
EOF

# orchestration/pipeline.py
cat > orchestration/pipeline.py << 'EOF'
from ingestion.text_ingest import TextIngestor
from normalization.cleaner import clean_text
from normalization.segmented import segment_text
from normalization.tokenizer import tokenize
from feature_extraction.vectorizer import bow_vector
from feature_extraction.embeddings import dummy_embeddings
from feature_extraction.stats_features import stats_features
from models.loader import load_models
from models.scorer import score_prediction
from structured_engine.intent_classifier import IntentClassifier
from structured_engine.hunter import Hunter
from post_processing.confidence import adjust_confidence
from post_processing.output_normalizer import normalize_output
from post_processing.result_mapper import map_result
from orchestration.state_tracker import StateTracker
from utils.logging import get_logger

logger = get_logger(__name__)


class Pipeline:
    def __init__(self):
        self.text_ingestor = TextIngestor()
        self.models = load_models()
        self.intent_classifier = IntentClassifier()
        self.hunter = Hunter()
        self.state_tracker = StateTracker()

    def run(self, input_data: dict) -> dict:
        logger.info("Pipeline starting")

        # Ingestion
        ingested = self.text_ingestor.ingest(input_data.get("text", ""))
        self.state_tracker.log_state("ingestion", ingested)

        # Normalization
        cleaned = clean_text(ingested["text"])
        segments = segment_text(cleaned)
        tokens = tokenize(cleaned)
        norm_data = {"cleaned": cleaned, "segments": segments, "tokens": tokens}
        self.state_tracker.log_state("normalization", norm_data)

        # Feature extraction
        bow = bow_vector(tokens)
        embeds = dummy_embeddings(tokens)
        stats = stats_features(tokens)
        features = {"bow": bow, "embeddings": embeds, "stats": stats}
        self.state_tracker.log_state("feature_extraction", features)

        # Model prediction
        classifier = self.models.get("rule_classifier")
        raw_pred = classifier.predict({"stats": stats})
        self.state_tracker.log_state("model_prediction", raw_pred)

        # Intent classification
        intent = self.intent_classifier.classify_intent(cleaned)
        routed = self.hunter.hunt({"prediction": raw_pred, "intent": intent})
        self.state_tracker.log_state("structured_engine", routed)

        # Post-processing
        scored = score_prediction(raw_pred)
        adjusted_conf = adjust_confidence(scored["confidence"], intent)
        scored["confidence"] = adjusted_conf
        normalized = normalize_output(scored)
        final_result = map_result(normalized, intent)
        self.state_tracker.log_state("post_processing", final_result)

        logger.info("Pipeline finished")
        return final_result
EOF

# utils/config.py
cat > utils/config.py << 'EOF'
CONFIG = {
    "app_name": "Microfyxd-ML",
    "version": "0.1.0",
}
EOF

# utils/exceptions.py
cat > utils/exceptions.py << 'EOF'
class MicrofyxdError(Exception):
    """Base exception for Microfyxd-ML."""
EOF

# utils/logging.py
cat > utils/logging.py << 'EOF'
import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] %(name)s %(levelname)s: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
EOF

# utils/metrics.py
cat > utils/metrics.py << 'EOF'
from utils.logging import get_logger

logger = get_logger(__name__)


def log_metric(name: str, value: float) -> None:
    logger.info(f"Metric {name}: {value}")
EOF

# utils/types.py
cat > utils/types.py << 'EOF'
from typing import Dict, Any

JsonDict = Dict[str, Any]
EOF

echo "Microfyxd-ML full build complete. Run: python main.py"
