# gomal-urdu-rag

Building a scalable RAG pipeline for Urdu low-resource language.
This is my FYP at Gomal University DI Khan, BS AI 7th sem.

## What this does
- Scrapes Urdu Wikipedia
- Cleans with Spark (parquet)
- Builds RDF Knowledge Graph
- Next: Qdrant vector DB + RAG API

## Why?
Urdu has no good structured dataset. Goal is to make a pipeline that can handle 100k docs, not just 100.

## Tech
Python, PySpark, RDFLib, Neo4j (later), Qdrant

## Current status
Phase 1 done: Scraper + Spark cleaning + KG turtle file

## How to run
pip install -r requirements.txt
python src/ingestion/scrape_wikipedia_urdu.py
python src/ingestion/spark_cleaning.py
python src/kg/build_kg.py