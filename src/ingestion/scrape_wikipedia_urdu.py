import requests
from bs4 import BeautifulSoup
import json
import os
import time

def scrape_urdu_wikipedia(num_articles=100):
    api_url = f"https://ur.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit={num_articles}&format=json"
    headers = {'User-Agent': 'Gomal-BSAI-Research-DEAI'}
    
    print("Fetching random Urdu article list...")
    resp = requests.get(api_url, headers=headers).json()
    articles = []
    
    for item in resp['query']['random']:
        title = item['title']
        content_url = f"https://ur.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext&titles={title}&format=json"
        try:
            c = requests.get(content_url, headers=headers).json()
            pages = c['query']['pages']
            for pid in pages:
                text = pages[pid].get('extract','')
                if len(text) > 500:
                    articles.append({
                        'title': title, 
                        'text': text, 
                        'url': f"https://ur.wikipedia.org/wiki/{title}"
                    })
                    print(f"Got: {title} - {len(text)} chars")
        except Exception as e:
            print(f"Skip {title}: {e}")
            continue
        time.sleep(0.5)
    
    os.makedirs('data/raw', exist_ok=True)
    with open('data/raw/urdu_wiki_raw.json','w',encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    
    print(f"\n--- SAVED {len(articles)} articles to data/raw/urdu_wiki_raw.json ---")
    return articles

if __name__ == "__main__":
    scrape_urdu_wikipedia(50)