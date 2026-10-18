# Paper 1: Scalable ETL for Urdu

Abstract: Urdu is low-resource. We built a pipeline using Wikipedia API + Spark + RDF. Processed 50 docs, 200+ triples. Future work to scale to 100k.

Method:
- Ingestion: Random API of Urdu Wikipedia
- Cleaning: Spark filter len>500, trim, parquet
- KG: RDFLib, custom namespace gomal.edu.pk/kg

Result: Table of raw vs clean count

Future: Add vector DB and LLM eval

References: Will add 5 papers on RAG + low-resource