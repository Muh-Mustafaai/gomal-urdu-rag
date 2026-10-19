import requests, json
from bs4 import BeautifulSoup

titles = ["کرنل شیر کلی", "Karnal Sher Khan", "پشاور", "ڈیرہ اسماعیل خان", "غزوہ بدر"]

headers = {'User-Agent': 'Mozilla/5.0'}
all_docs = []

for title in titles:
    url = f"https://ur.wikipedia.org/wiki/{title}"
    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        paras = soup.select('p')
        text = "\n".join([p.get_text() for p in paras[:5]])
        if len(text) > 100:
            print(f"✓ Scraped: {title}")
            all_docs.append({"title": title, "text": text, "text_clean": text, "url": url})
    except Exception as e:
        print(f"X Failed {title}: {e}")

# Add to existing clean file
with open("data/processed/urdu_wiki_clean.json", 'r', encoding='utf-8') as f:
    old = json.load(f)

old.extend(all_docs)

with open("data/processed/urdu_wiki_clean.json", 'w', encoding='utf-8') as f:
    json.dump(old, f, ensure_ascii=False, indent=2)

print(f"Total docs now: {len(old)}")
print("Now re-run: python src/ingestion/generate_embeddings.py")