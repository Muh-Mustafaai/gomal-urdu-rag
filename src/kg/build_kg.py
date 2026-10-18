from rdflib import Graph, Namespace, Literal, URIRef
import json
import os

# we are building a simple RDF graph here
# idea is to turn each wiki article into a node with title and url

g = Graph()
GU = Namespace("http://gomal.edu.pk/kg/")
g.bind("gu", GU)

# path to raw file we scraped earlier
json_path = "data/raw/urdu_wiki_raw.json"

if not os.path.exists(json_path):
    print("raw json not found, run scraper first")
    exit()

print("loading raw json...")

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"total articles loaded: {len(data)}")

# loop and make triples
# each article becomes Article_0, Article_1 etc
for i, art in enumerate(data):
    # make a unique URI for this article
    subj = URIRef(GU[f"Article_{i}"])
    
    # add title triple
    g.add((subj, GU.title, Literal(art['title'])))
    # add url triple
    g.add((subj, GU.url, Literal(art['url'])))
    # language is urdu
    g.add((subj, GU.language, Literal("ur")))
    
    # simple length triple, useful for filtering later
    g.add((subj, GU.textLength, Literal(len(art['text']))))

# make sure kg folder exists
os.makedirs("data/kg", exist_ok=True)

# save as turtle format, easy to view
output_path = "data/kg/gomal_kg.ttl"
g.serialize(output_path, format="turtle")

print(f"done! KG saved with {len(g)} triples at {output_path}")
# you can open this .ttl file and see the graph