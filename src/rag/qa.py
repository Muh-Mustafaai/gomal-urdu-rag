import json

with open("data/processed/urdu_wiki_clean.json", encoding='utf-8') as f:
    db = json.load(f)

# Simple search from before
def search(query):
    for d in db:
        if d['title'] in query or query.replace("کون تھا؟","").strip() in d['title'] or "شیر کلی" in query and "شیر کلی" in d['title']:
            return d
    return db[0]

# Mock LLM answer (for demo — later replace with real LLM)
def answer_urdu(query):
    doc = search(query)
    print(f"\nQ: {query}")
    print(f"Retrieved: {doc['title']}")
    print(f"\nContext: {doc.get('text','')[:400]}...")
    
    # For demo, you can use Groq/OpenAI API for Urdu answer
    # For now, just return context as answer
    print(f"\n--- ANSWER (from RAG) ---\n{doc.get('text','')[:500]}")

answer_urdu("کرنل شیر کلی کون تھا؟")