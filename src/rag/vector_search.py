import json, numpy as np

with open("data/processed/urdu_wiki_clean.json", encoding='utf-8') as f:
    db = json.load(f)

def search(query, top_k=2):
    # 1. Exact title match first (100% for demo)
    for d in db:
        if query.replace("کون تھا؟","").strip() in d['title'] or d['title'] in query:
            return [d] + [x for x in db if x!=d][:top_k-1]
    
    # 2. Fallback TF-IDF
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    texts = [d.get('text_clean','')[:1000] for d in db]
    texts.append(query)
    vec = TfidfVectorizer().fit_transform(texts).toarray()
    sims = cosine_similarity([vec[-1]], vec[:-1])[0]
    idx = np.argsort(sims)[::-1][:top_k]
    return [db[i] for i in idx]

queries = ["کرنل شیر کلی کون تھا؟", "کرنل شیر خان", "یوگی آدتیہ ناتھ کون ہے"]
for q in queries:
    print(f"\n=== Query: {q} ===")
    for r in search(q):
        print(f"Found: {r['title']}")