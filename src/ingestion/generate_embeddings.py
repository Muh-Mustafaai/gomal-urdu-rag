import json, os
print("Using sklearn TF-IDF embeddings (no torch, no fastembed) - works 100%")

from sklearn.feature_extraction.text import TfidfVectorizer

with open("data/processed/urdu_wiki_clean.json", 'r', encoding='utf-8') as f:
    docs = json.load(f)

print(f"Loaded {len(docs)} docs")
texts = [(d.get('text_clean') or d.get('text',''))[:1000] for d in docs]

print("Generating TF-IDF vectors...")
vectorizer = TfidfVectorizer(max_features=384)
embeddings = vectorizer.fit_transform(texts).toarray()

print(f"Embeddings shape: {embeddings.shape}")

os.makedirs("data/embeddings", exist_ok=True)
out = []
for i, d in enumerate(docs):
    out.append({
        "title": d.get('title'),
        "text": texts[i][:500],
        "embedding": embeddings[i].tolist()
    })

with open("data/embeddings/urdu_embeddings.json", 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"DONE! Saved {len(out)} embeddings to data/embeddings/urdu_embeddings.json")