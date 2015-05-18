# searchpage
# Zoekt de juiste pagina
# input: lijst Y
# output: juiste dbpedia pagina

def searchPage(y):
    y = " ".join(y)

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

                    return uri

       
