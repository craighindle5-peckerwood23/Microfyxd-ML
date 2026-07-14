from typing import List

def compute_embeddings(text: str) -> List[float]:
    length = len(text)
    vowels = sum(1 for c in text.lower() if c in "aeiou")
    return [float(length), float(vowels)]
