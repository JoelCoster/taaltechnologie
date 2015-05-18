# Vraag- antwoordsysteem
# Jasper de Boer s1889966
import socket
import sys
import lxml
from lxml import etree

import csv
from SPARQLWrapper import SPARQLWrapper, JSON

eigenschappen = {'geboortedatum': "dbpedia-owl:birthDate",
                 'naam': "dbpedia-owl:longName",
                 'beroep': "prop-nl:beroep",
                 'label': "dbpedia-owl:parentOrganisation ",
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

def showExampleQuestions():
    print("Stel vragen over de schrijver van een nummer. Bijvoorbeeld:")
    print("Door wie werd Bohemian Rhapsody geschreven?")
    print("Wie is de schrijver van You'll Never Walk Alone?")
    print("Wie schreef Bohemian Rhapsody?")
    print("Wie heeft Mamma Mia geschreven?")
    print(".. Stel alleen vragen over bekende nummers")

def getXgetY(question):
    posVan = question.index("van")
    
    x = " ".join(question[3:posVan])
    y = " ".join(question[posVan+1:])
            
    return [x,y]

def answerQuestion(resource,x):
    query = "SELECT STR(?output) WHERE { <"+uri+"> "+eigenschappen[x]+" ?output }"
    sparql = SPARQLWrapper("http://nl.dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    
    return sparql.query().convert()

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

while True:
    
    question = input("Vraag: ").replace("?","")

    if question == "":
        showExampleQuestions()
        
    else:

        xml = alpino_parse(question)

        root = xml.xpath('//node[@cat="mwu" and @rel="obj1"]')
        for node in root:
            if "mwu_root" in node.attrib:
               y = node.attrib["mwu_root"]

        root = xml.xpath('//node[@cat="mwu" and @rel="su"]')
        for node in root:
            if "mwu_root" in node.attrib:
                y = node.attrib["mwu_root"]

        root = xml.xpath('//node[@cat="ppart" and @rel="vc"]/node[@rel="obj1"]')
        for node in root:
            if "lemma" in node.attrib:
                y = node.attrib["lemma"]

        root = xml.xpath('//node[@lemma="schrijven"]')
        for node in root:
            if "lemma" in node.attrib:
                x = node.attrib["lemma"]
            
        root = xml.xpath('//node[@cat="np" and @rel="su"]/node[@word]')
        for node in root:
            if "lemma" in node.attrib:
                if node.attrib["lemma"] != "de":
                    x = node.attrib["lemma"]
        if x == "schrijven":
            x = "schrijver"

        if x == "" or y == "":
            print("Parsen van de zin mislukt")

        else:

            if x.lower() in eigenschappen:

                question = question.split(" ")

                with open('anchor_summary.csv', 'r') as anchorfile:
                    anchor_summarycsv = csv.reader(anchorfile, delimiter=',', quotechar='"')
                    for regel in anchor_summarycsv:
                        if regel[0].lower() == y.lower():
                            pages = str.split(regel[1],";")
                            page = str.split(pages[0],":")[0]
                            break
                            
                resource = False

                with open('page.csv', 'r') as pagefile:
                    pagecsv = csv.reader(pagefile, delimiter=',', quotechar='"')
                    for line in pagecsv:
                        if line[0] == page:
                            resource = line[1].replace(" ","_")
                            break
                if resource:
                    uri = "http://nl.dbpedia.org/resource/"+resource
                    results = answerQuestion(uri,x.lower())
                    i = 0
                    for result in results["results"]["bindings"]:
                        for arg in result:
                            print(result[arg]["value"])
                            i+=1

                    if i == 0:
                        print("Ik kan het niet vinden")

                    resource = False
                    page = False

                else:
                    print("Ik weet niet wie of wat "+y+" is")

            else:
                print("Ik weet niet wat '"+x+"' betekent")

            x = ""
            y = ""
                



