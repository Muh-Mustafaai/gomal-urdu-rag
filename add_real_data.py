import json

real_karnal = {
    "title": "کرنل شیر خان",
    "url": "manual",
    "text": """کرنل شیر خان (1970-1999) پاکستان آرمی کے ایک بہادر افسر تھے جنہیں نشان حیدر سے نوازا گیا۔ 
    وہ 1 جنوری 1970 کو صوابی میں پیدا ہوئے۔ 1999 میں کارگل جنگ میں انہوں نے بہادری سے دشمن کا مقابلہ کیا۔
    انہوں نے بھارتی فوج کے کئی حملے ناکام بنائے اور آخر کار 5 جولائی 1999 کو شہید ہو گئے۔
    بھارتی فوج نے بھی ان کی بہادری کو تسلیم کیا اور کہا کہ وہ شیر کی طرح لڑے۔
    ان کا تعلق صوابی، خیبر پختونخوا سے تھا۔ وہ پاکستان کے سب سے کم عمر نشان حیدر وصول کنندگان میں سے ہیں۔""",
    "text_clean": """کرنل شیر خان (1970-1999) پاکستان آرمی کے ایک بہادر افسر تھے جنہیں نشان حیدر سے نوازا گیا۔ 
    وہ 1 جنوری 1970 کو صوابی میں پیدا ہوئے۔ 1999 میں کارگل جنگ میں انہوں نے بہادری سے دشمن کا مقابلہ کیا۔
    انہوں نے بھارتی فوج کے کئی حملے ناکام بنائے اور آخر کار 5 جولائی 1999 کو شہید ہو گئے۔"""
}

with open("data/processed/urdu_wiki_clean.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

# Remove old village entry if exists
data = [d for d in data if d['title'] != 'کرنل شیر کلی']

data.append(real_karnal)
data.append({"title": "کرنل شیر کلی", "url": "manual", "text": real_karnal["text"], "text_clean": real_karnal["text_clean"]})

with open("data/processed/urdu_wiki_clean.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Added real Karnal Sher Khan data!")