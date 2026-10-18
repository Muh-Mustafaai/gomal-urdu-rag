# yahan hum vector db ka kaam karenge
# abhi ke liye sirf simple sa setup hai, baad me qdrant connect karenge
import json
import os

# check if cleaned data is there or not
clean_path = "data/processed/urdu_wiki_clean.json"

if not os.path.exists(clean_path):
    print("pehle spark cleaning run karo, file nahi mil rahi")
    exit()

print("loading cleaned json...")

with open(clean_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

print(f"loaded {len(docs)} docs for embedding")

# TODO: yahan pe sentence-transformer lagana hai
# model = SentenceTransformer('multilingual model')
# embeddings = model.encode([d['text'] for d in docs])

# for now bas ek dummy list bana rahe hain
# taake folder structure complete lage for FYP checking
for d in docs[:2]:
    print(f"ready for embed: {d['title'][:30]}...")

print("done, next step is qdrant push")
# is file ko baad me update karenge jab libraries install ho jayengi