import pytesseract
from PIL import Image

class OCRIngest:
    def extract(self, image_path):
        text = pytesseract.image_to_string(Image.open(image_path))
        return {"source": "ocr", "content": text}