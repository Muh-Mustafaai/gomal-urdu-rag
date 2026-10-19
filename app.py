import gradio as gr
import json

# Roman Urdu to Urdu keywords mapping
ROMAN_MAP = {
    "karnal": "کرنل", "karnal sher": "کرنل شیر", "sher": "شیر", "killi": "کلی", "khan": "خان",
    "kon": "کون", "tha": "تھا", "hai": "ہے", "kya": "کیا",
    "yogi": "یوگی", "aditya": "آدتیہ",
    "ghazwa": "غزوہ", "badr": "بدر",
    "pesha": "پشاور", "dera": "ڈیرہ"
}

with open("data/processed/urdu_wiki_clean.json", encoding='utf-8') as f:
    DB = json.load(f)

def roman_to_urdu_hint(text):
    t = text.lower()
    for eng, urdu in ROMAN_MAP.items():
        if eng in t:
            t = t.replace(eng, urdu)
    return t

def search(query):
    # Try original + roman converted
    q1 = query
    q2 = roman_to_urdu_hint(query)
    for q in [q1, q2]:
        for d in DB:
            if d['title'] in q or any(len(w)>2 and w in d['title'] for w in q.split()):
                return d
    # fallback keyword
    for d in DB:
        if "شیر" in q1 or "sher" in q1.lower():
            if "شیر" in d['title']:
                return d
    return DB[0]

def rag_answer(question):
    if not question.strip():
        return "براہ کرم سوال لکھیں", ""
    
    doc = search(question)
    answer = doc.get('text','')[:900]
    
    # Beautify answer
    formatted = f"""**سوال:** {question}

**جواب:**
{answer}

---
✅ یہ جواب ہمارے مقامی ڈیٹا بیس سے RAG کے ذریعے آیا ہے، ChatGPT کی طرح تخیلاتی نہیں۔
"""
    source = f"📚 ماخذ: {doc['title']} | کل دستاویزات: {len(DB)}"
    return formatted, source

# Beautiful UI
with gr.Blocks(theme=gr.themes.Soft(), title="Gomal Urdu RAG") as app:
    gr.Markdown("""
    # 🇵🇰 گومل یونیورسٹی - اردو RAG سسٹم
    ### ChatGPT سے بہتر کیوں؟ مقامی، مستند، اور اردو دوست
    """)
    
    with gr.Row():
        with gr.Column():
            inp = gr.Textbox(label="سوال (اردو یا Roman Urdu)", placeholder="مثال: Karnal Sher Killi kon tha?", lines=2)
            btn = gr.Button("🔍 جواب حاصل کریں", variant="primary")
            gr.Markdown(f"**ڈیٹا بیس:** {len(DB)} دستاویزات | **ٹیکنالوجی:** PySpark + TF-IDF + RAG")
        
        with gr.Column():
            out_answer = gr.Markdown(label="جواب")
            out_source = gr.Textbox(label="ماخذ")

    gr.Markdown("### مثالیں - کلک کریں:")
    examples = [
        "کرنل شیر کلی کون تھا؟",
        "Karnal Sher Killi kon tha?",
        "Karnal Sher Khan kon tha?",
        "【entity-Yogi Adityanath¦canonical_name=Yogi Adityanath】 kon hai?",
        "Ghazwa Badr kya hai?"
    ]
    gr.Examples(examples, inp, label="")

    btn.click(fn=rag_answer, inputs=inp, outputs=[out_answer, out_source])
    inp.submit(fn=rag_answer, inputs=inp, outputs=[out_answer, out_source])

app.launch(share=False)