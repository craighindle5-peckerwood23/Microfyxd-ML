class IntentClassifier:
    def classify(self, text):
        if "refund" in text.lower():
            return "refund_request"
        if "schedule" in text.lower():
            return "scheduling"
        return "general"