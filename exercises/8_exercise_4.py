import csv
import hashlib
import rdflib 
from rdflib.namespace import XSD, RDF, RDFS
from rdflib import URIRef, Literal, Namespace

g = rdflib.Graph()
WD = Namespace("http://www.wikidata.org/entity/")
WDT = Namespace("http://www.wikidata.org/prop/direct/")

with open('8_artist_data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        artist_label = row["name"]
        artist_uri = "http://example.org/"+hashlib.md5(artist_label.encode('utf-8')).hexdigest()
        gender_label = row["gender"]
        gender_uri = "http://example.org/"+row["gender"].lower()
        birth_year = row["yearOfBirth"]
        death_year = row["yearOfDeath"]
        birth_place_label = row["placeOfBirth"]
        birth_place_uri = hashlib.md5(birth_place_label.encode('utf-8')).hexdigest()
        death_place_label = row["placeOfDeath"]
        death_place_uri = hashlib.md5(death_place_label.encode('utf-8')).hexdigest()
        url = row["url"]

        g.add(( URIRef(artist_uri), RDFS.label , Literal(artist_label) ))

        g.add(( URIRef(artist_uri), WDT.P21 , URIRef(gender_uri) ))
        g.add(( URIRef(gender_uri), RDFS.label , Literal(gender_label) ))

        if len(birth_year) > 0:
            g.add(( URIRef(artist_uri), WDT.P569 , Literal(birth_year) ))
        if len(death_year) > 0:
            g.add(( URIRef(artist_uri), WDT.P570 , Literal(death_year) ))

        g.add(( URIRef(artist_uri), WDT.P19 , URIRef(birth_place_uri) ))
        g.add(( URIRef(birth_place_uri), RDFS.label , Literal(birth_place_label) ))

        g.add(( URIRef(artist_uri), WDT.P20 , URIRef(death_place_uri) ))
        g.add(( URIRef(death_place_uri), RDFS.label , Literal(death_place_label) ))

        g.add(( URIRef(artist_uri), WDT.P973 , URIRef(url) ))
        if "id" in row:
            g.add(( URIRef(artist_uri), WDT.P2741 , URIRef("https://www.tate.org.uk/art/artists/"+row["id"]) ))

for s,p,o in g.triples((None, None, None)):
    print(s,p,o)

g.serialize(destination="8_exercise_4.ttl", format="ttl")