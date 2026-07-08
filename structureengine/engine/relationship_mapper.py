class RelationshipMapper:
    def map(self, entities):
        return {"relationships": [{"entity": e["text"], "type": e["label"]} for e in entities]}