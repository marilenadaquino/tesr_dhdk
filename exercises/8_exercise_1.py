import rdflib
from rdflib import URIRef, Literal
from rdflib.namespace import XSD
from rdflib import Namespace

DBO = Namespace("http://dbpedia.org/ontology/")

example_data = """
    <http://example.org/robert_capa> <http://example.org/knows> <http://example.org/henri_cartier_bresson> .
    <http://example.org/gerda_taro> <http://example.org/hasSpouse> <http://example.org/robert_capa> .
    """
g = rdflib.Graph()

# parse data from string
g.parse(data=example_data, format='nt')
# get the number of statements (triples)
print(len(g))

# parse data from file
g.parse("7_robert_capa.rdf", format="xml")
print(len(g))

# parse data from URI
g.parse("https://dbpedia.org/resource/Robert_Capa")
print(len(g))

# print all triples
#for s, p, o in g.triples((None, None, None )):
#    print(s,p,o)

# print triples where a certain URI is subject
for s, p, o in g.triples(( URIRef("http://dbpedia.org/resource/Photojournalism"), None, None )):
    print(s,p,o)

# print all the values of a certain property
for s, p, o in g.triples(( URIRef("http://dbpedia.org/resource/Robert_Capa"), URIRef("http://dbpedia.org/property/birthName"), None )):
    print(s,p,o)

# print all the properties of a certain value
for s, p, o in g.triples(( None, None, Literal("1954-05-25",datatype=XSD.date) )):
    print(s,p,o)

# print all the values of a certain property
for s, p, o in g.triples(( None, DBO.birthDate, None )):
    print(s,p,o)

g.add(( URIRef("http://dbpedia.org/resource/Robert_Capa"), 
        DBO.occupation, 
        URIRef("http://dbpedia.org/resource/Photographer") ))

g.remove(( URIRef("http://dbpedia.org/resource/Robert_Capa"), 
        DBO.occupation, 
        URIRef("http://dbpedia.org/resource/Photographer") ))

for s,p,o in g.triples(( None, DBO.occupation, None )):
	print(s,p,o)

g.serialize(destination="8_exercise_1.ttl", format="turtle")

