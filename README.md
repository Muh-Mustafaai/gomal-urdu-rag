# Gomal Urdu RAG - FYP 2025

## 🇵🇰 Scalable Urdu Retrieval-Augmented Generation System for Low-Resource Language

**BS AI, Gomal University, DI Khan | Batch 2023-27**

### Overview
A domain-specific RAG pipeline for Urdu language queries, focused on local history (Karnal Sher Khan, DI Khan region). Built to address hallucination in general LLMs like ChatGPT for Urdu.

### Why not ChatGPT?
- ChatGPT hallucinates local history & weak in Roman Urdu
- Our system is **verified, offline-capable, and domain-specific**
- No API cost, works for schools in KP with no internet

### Architecture
1. **Scraping:** Urdu Wikipedia (Custom scraper for 100+ docs)
2. **Cleaning:** PySpark distributed cleaning (5.5GB heap config)
3. **Embeddings:** TF-IDF with Urdu tokenization
4. **Vector Search:** Cosine similarity + title matching
5. **RAG QA:** Retrieval -> Context -> Answer
6. **UI:** Gradio with Roman Urdu -> Urdu mapping

### Challenges Solved
- Issue: Urdu Wikipedia page "Karnal Sher Killi" contained village data, not hero data
- Solution: Implemented data curation layer with manually verified dataset for Nishan-e-Haider heroes

### Results
- Query: "Karnal Sher Killi kon tha?" -> Correct answer with source
- Supports both Urdu script and Roman Urdu

### Tech Stack
Python, PySpark, Scikit-learn, Gradio, JSON



### Author
Mustafa - BS AI Gomal 