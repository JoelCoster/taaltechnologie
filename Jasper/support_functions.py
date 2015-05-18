def getProperty(inputString):
    
    properties = {'geboortedatum': "dbpedia-owl:birthDate",
                  'geboren': "dbpedia-owl:birthDate",
                  'naam': "dbpedia-owl:longName",
                  'beroep': "prop-nl:beroep",
                  'label': "dbpedia-owl:parentOrganisation",
                  'geloof': "prop-nl:geloof",
                  'website': "foaf:homepage",
                  'ouders': "prop-nl:ouders",
                  'partner': "prop-nl:partner",
                  'sterfdatum': "dbpedia-owl:deathDate",
                  'bijnaam': "foaf:nick",
                  'bandleden': "dbpedia-owl:bandMember",
                  'leden': "dbpedia-owl:bandMember",
                  'artiest': "dbpedia-owl:artist",
                  'schrijver': "dbpedia-owl:musicalArtist"}

    try:
        found = properties[inputString.lower().strip()]
    except:
        found = ""

    return found

def makeQuery(property, uri, modifiers):

    query = "SELECT STR(?output) WHERE { <"+uri+"> "+"bandleden"+" ?output }"
    sparql = SPARQLWrapper("http://nl.dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    
    print(sparql.query().convert())
    



makeQuery("x", "http://nl.dbpedia.org/resource/U2_(band)", "a")
