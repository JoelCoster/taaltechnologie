from SPARQLWrapper import SPARQLWrapper, JSON

def getProperty(inputString):

    inputString = " ".join(inputString)

    properties = {'geboortedatum': "dbpedia-owl:birthDate",
                  'zijn geboren': "dbpedia-owl:birthDate",
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
                  'lid': "dbpedia-owl:bandMember",
                  'artiest': "dbpedia-owl:artist",
                  'schrijver': "dbpedia-owl:musicalArtist"}

    try:
        found = properties[inputString.lower().strip()]
    except:
        found = ""

    return found





def makeQuery(property, resource, modifiers):

	query = "SELECT STR(?output) WHERE { <http://nl.dbpedia.org/resource/"+resource+"> "+property+" ?output }"
	
	return query
