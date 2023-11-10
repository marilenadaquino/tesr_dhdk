import json
import hashlib
import rdflib 
from rdflib.namespace import XSD, RDF, RDFS
from rdflib import URIRef, Literal, Namespace


import json
 
with open('8_vendetta.json', 'r') as f:
    data = json.load(f)

description = data["description"]
title = data["title"]

authors_ids = []
for k,v in data.items():
    if k == "authors":
        for person in v:
            author_id = person["author"]["key"]
            authors_ids.append(author_id)

genres = data["subjects"]

# create a graph
g = rdflib.Graph()

# namespaces
SCHEMA = Namespace("http://schema.org/")

# design opaque URIs
book_id = hashlib.md5(title.encode('utf-8')).hexdigest()
book_uri = "http://w3id.org/example/"+book_id

# add triples
g.add(( URIRef(book_uri), RDF.type, SCHEMA.CreativeWork ))
g.add(( URIRef(book_uri), RDFS.label, Literal(title) ))
g.add(( URIRef(book_uri), SCHEMA.headline, Literal(title) ))
g.add(( URIRef(book_uri), SCHEMA.abstract, Literal(description) ))

for author in authors_ids:
    author_uri = "http://w3id.org/example"+author
    g.add(( URIRef(book_uri), SCHEMA.creator, URIRef(author_uri) ))

for genre in genres:
    genre_uri = "http://w3id.org/example/"+hashlib.md5(genre.encode('utf-8')).hexdigest()
    g.add(( URIRef(book_uri), SCHEMA.genre, URIRef(genre_uri) ))
    g.add(( URIRef(genre_uri), RDFS.label, Literal(genre) ))

for s,p,o in g.triples((None, None, None)):
    print(s,p,o)

g.serialize(destination="8_exercise_3.json", format="json-ld")