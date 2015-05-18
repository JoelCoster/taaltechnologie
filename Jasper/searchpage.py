import csv
from SPARQLWrapper import SPARQLWrapper, JSON

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

