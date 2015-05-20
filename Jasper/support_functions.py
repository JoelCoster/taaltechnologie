from SPARQLWrapper import SPARQLWrapper, JSON
import csv
import socket
import lxml
from lxml import etree

def getProperty(inputString):

    inputString = " ".join(inputString)

    properties = {'geboortedatum': "dbpedia-owl:birthDate",
                  'zijn geboren': "dbpedia-owl:birthDate",
                  'op_richten' : "dbpedia-owl:activeYearsStartYear",
                  'beginnen' : "dbpedia-owl:activeYearsStartYear",
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
                  'schrijver': "dbpedia-owl:musicalArtist",
                  'plaat_label' : "dbpedia-owl:parentOrganisation",
                  'uit_brengen' : "dbpedia-owl:releaseDate",
                  'verliet' : "dbpedia-owl:formerBandMember",
                  'spelen' = "dbpedia-owl:bandMember",
                  'oorsprong' = "dbpedia-owl:origin",
                  'overlijden' = "dbpedia-owl:deathDate",
                  'abstract' = "dbpedia-owl:abstract",
                  'samenvatting' = "dbpedia-owl:abstract",
                  'bezetting': "dbpedia-owl:bandMember",
                  'bezigheid' : "dbpedia-owl:occupation",
                  'beroep' : "dbpedia-owl:occupation"
   
                  }

    try:
        found = properties[inputString.lower().strip()]
    except:
        found = ""

    return found


def makeQuery(property, resource, modifiers):

    mod = "_".join(modifiers)

    modDict = { "hoe_veel" : "COUNT(STR(?output))"}

    if mod in modDict:
        select = modDict[mod]
    else:
        select = "STR(?output)"
    

    query = "SELECT "+select+" WHERE { <http://nl.dbpedia.org/resource/"+resource+"> "+property+" ?output }"
	
    return query

def alpino_parse(sent, host='zardoz.service.rug.nl', port=42424):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    sent = sent + "\n\n"
    sentbytes= sent.encode('utf-8')
    s.sendall(sentbytes)
    bytes_received= b''
    while True:
        byte = s.recv(8192)
        if not byte:
            break
        bytes_received += byte
    xml = etree.fromstring(bytes_received)
    return xml

def answerQuestion(query):
    sparql = SPARQLWrapper("http://nl.dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    
    return sparql.query().convert()


def searchPage(y):
    
    y = " ".join(y)

    with open('anchor_summary.csv', 'r') as anchorfile:

        anchor_summarycsv = csv.reader(anchorfile, delimiter=',', quotechar='"')
        page = ""
        
        for regel in anchor_summarycsv:

            if regel[0].lower() == y.lower():

                pages = str.split(regel[1],";")
                page = str.split(pages[0],":")[0]
                break

            resource = False

        if page != "":

            with open('page.csv', 'r') as pagefile:

                pagecsv = csv.reader(pagefile, delimiter=',', quotechar='"')

                for line in pagecsv:

                    if line[0] == page:

                        resource = line[1].replace(" ","_")
                        break
                    
                if resource:
                    
                    return resource


