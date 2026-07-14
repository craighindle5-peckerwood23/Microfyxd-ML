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
