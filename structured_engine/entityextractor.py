import spacy

nlp = spacy.load("en_core_web_sm")

class EntityExtractor:
    def extract(self, text):
        doc = nlp(text)
        return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
