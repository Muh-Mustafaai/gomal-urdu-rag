# simple cleaning without spark, coz java issue
# does same work as spark one but using pandas

import json
import os
import pandas as pd

raw_path = "data/raw/urdu_wiki_raw.json"
clean_path = "data/processed/urdu_wiki_clean.json"

print("loading raw data...")

with open(raw_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"raw count: {len(data)}")

# using pandas to clean
df = pd.DataFrame(data)

# basic cleaning - remove empty texts
df = df[df['text'].str.len() > 50]

# remove duplicates by title
df = df.drop_duplicates(subset=['title'])

# make processed folder if not there
os.makedirs("data/processed", exist_ok=True)

# save back
cleaned = df.to_dict(orient='records')

with open(clean_path, 'w', encoding='utf-8') as out:
    json.dump(cleaned, out, ensure_ascii=False, indent=2)

print(f"cleaned and saved {len(cleaned)} docs to {clean_path}")
print("done, no spark needed for now")