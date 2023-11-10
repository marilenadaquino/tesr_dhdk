import xml.etree.ElementTree as ET
import hashlib
import rdflib 
from rdflib.namespace import XSD, FOAF, RDF, RDFS
from rdflib import URIRef, Literal, Namespace

# parse xml file
root = ET.parse("8_orwell.xml")
# declare namespaces
ns = {"": "urn:isbn:1-931666-33-4"}

# name
name_container = root.find("cpfDescription/identity/nameEntry", ns)
orwell_name = name_container[0].text+", "+name_container[1].text

# dates
birth_date = root.find("cpfDescription/description/existDates/dateRange/fromDate", ns).attrib["standardDate"]
death_date = root.find("cpfDescription/description/existDates/dateRange/toDate", ns).attrib["standardDate"]

# bio
bio = root.find("cpfDescription/description/biogHist/p", ns).text

# relations
people = []
for person in root.findall("cpfDescription/relations/cpfRelation/relationEntry",ns):
    if person.text:
        clean_name = person.text.rsplit(',', 1)[0]
        people.append(clean_name)

# design opaque ID and URIs for people
orwell_id = hashlib.md5(orwell_name.encode('utf-8')).hexdigest()
orwell_uri = "http://w3id.org/example/"+orwell_id

people_ids = {}
for pers in people:
    pers_id = hashlib.md5(pers.encode('utf-8')).hexdigest()
    pers_uri = "http://w3id.org/example/"+pers_id
    people_ids[pers] = pers_uri

# create a graph
g = rdflib.Graph()

# namespaces
DBO = Namespace("http://dbpedia.org/ontology/")

# populate the grap with entities and their class
g.add(( URIRef(orwell_uri), RDF.type, FOAF.Person ))
g.add(( URIRef(orwell_uri), RDFS.label, Literal(orwell_name) ))
g.add(( URIRef(orwell_uri), DBO.abstract, Literal(bio) ))
g.add(( URIRef(orwell_uri), DBO.birthDate, Literal(birth_date, datatype=XSD.date) ))
g.add(( URIRef(orwell_uri), DBO.deathDate, Literal(death_date, datatype=XSD.date) ))

for pers_name, pers_uri in people_ids.items():
    g.add(( URIRef(pers_uri), RDF.type, FOAF.Person ))
    g.add(( URIRef(pers_uri), RDFS.label, Literal(pers_name) ))
    g.add(( URIRef(orwell_uri), FOAF.knows, URIRef(pers_uri) ))

for s,p,o in g.triples((None, None, None)):
    print(s,p,o)

g.serialize(destination="8_exercise_2.ttl", format="turtle")