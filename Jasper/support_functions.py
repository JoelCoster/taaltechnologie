from SPARQLWrapper import SPARQLWrapper, JSON
import csv
import socket
import lxml
from lxml import etree

def getProperty(inputString):

    inputString = "_".join(inputString)

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
                  'spelen' : "dbpedia-owl:bandMember",
                  'oorsprong' : "dbpedia-owl:origin",
                  'overlijden' : "dbpedia-owl:deathDate",
                  'abstract' : "dbpedia-owl:abstract",
                  'samenvatting' : "dbpedia-owl:abstract",
                  'bezetting': "dbpedia-owl:bandMember",
                  'bezigheid' : "dbpedia-owl:occupation",
                  'beroep' : "dbpedia-owl:occupation",
                  'duur' : "dbpedia-owl:playingTime",
                  'lengte' : "dbpedia-owl:playingTime",
                  'duur_lengte' : "dbpedia-owl:playingTime",
                  'afspeeltijd' : "dbpedia-owl:playingTime",
                  'speeltijd' : "dbpedia-owl:playingTime",
                  'echte_volledige': "dbpedia-owl:longName",
                  'echt_naam': "dbpedia-owl:longName",
                  'geboortedag': "dbpedia-owl:birthDate",
                  'geloofsovertuiging': "prop-nl:geloof",
                  'genre': "prop-nl:genre",
                  'stijl': "prop-nl:genre",
                  'muziek_stijl': "prop-nl:genre",
                  'herkomst_plaats' : "dbpedia-owl:origin",
                  'herkomst' : "dbpedia-owl:origin",
                  'web_site': "foaf:homepage",
                  'doodsoorzaak' : "prop-nl:oorzaakDood",
                  'oorzaak' : "prop-nl:oorzaakDood",
                  'oprichting_datum' : "dbpedia-owl:activeYearsStartYear",
                  'platenmaatschappij' : "dbpedia-owl:parentOrganisation",
                  'geloof': "prop-nl:religie",
                  "echt_naam" : "dbpedia-owl:longName",
                  "zijn_geboren_geboren" : "dbpedia-owl:birthDate",
                  "instrument_bespelen" : "dbpedia-owl:instrument",
                  "in_band_spelen": "dbpedia-owl:bandMember",
                  "muziek_label": "prop-nl:recordLabel",
                  "bespelen": "dbpedia-owl:instrument",
                  "geheel_naam" : "dbpedia-owl:longName",
                  "kind" : "prop-nl:kinderen",
                  "album": "dbpedia-owl:album",
                  "volledig_naam": "dbpedia-owl:longName",
                  "met_trouwen": "prop-nl:partner",
                  "lengte": "dbpedia-owl:playingTime",
                  "zingen": "dbpedia-owl:musicalArtist",
                  "uit_brengen" : "prop-nl:recordLabel",
                  "uit_geven": "prop-nl:recordLabel",
                  "in_band_zitten": "dbpedia-owl:bandMember",
                  "land": "dbpedia-owl:country",
                  "huidig_lid": "dbpedia-owl:bandMember",
                  "geboorte_naam": "dbpedia-owl:longName",
                  "instrument_bespelen": "dbpedia-owl:instrument ",
                  "uitgever": "prop-nl:recordLabel",
                  "uit_stad_komen" : "dbpedia-owl:country",
                  "uit_land_komen" : "dbpedia-owl:country",
                  'plaat_maatschappij' : "prop-nl:recordLabel",
                  'start_datum' : "dbpedia-owl:activeYearsStartYear",
                  'sterf_dag': "dbpedia-owl:deathDate",
                  'sterven_dag': "dbpedia-owl:deathDate",
                  'url': "foaf:homepage",
                  "instrument" : "dbpedia-owl:instrument",
                  'beginjaar' : "dbpedia-owl:activeYearsStartYear",
                  'budget' : "prop-nl:budget",
                  'nummer' : "dbpedia-owl:Single",
                  'single' : "dbpedia-owl:Single",
                  'liedje' : "dbpedia-owl:Single",
                  'lied' : "dbpedia-owl:Single",
                  'plaat' : "dbpedia-owl:Single",
                  'album' : "dbpedia-owl:Album",
                  'cd' : "dbpedia-owl:Album"
                  }

    try:
        found = properties[inputString.lower().strip()]
    except:
        found = ""

    return found


def makeQuery(property, resource, modifiers, order):

    mod = "_".join(modifiers)

    modDict = { "hoe_veel" : "COUNT(STR(?output))"}

    if order != "":

        query = "SELECT ?output WHERE { ?output prop-nl:artiest <http://nl.dbpedia.org/resource/"+resource+"> . ?output "+order[1]+" ?order } ORDER BY "+order[0]+"(?order) LIMIT 1"

    else:

        if mod in modDict:
            select = modDict[mod]
        else:
            select = "STR(?output)"
        
        query = "SELECT "+select+" WHERE { <http://nl.dbpedia.org/resource/"+resource+"> "+property+" ?output }"

    print(query)
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


