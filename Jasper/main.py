# Eindopdracht Taaltechnologie
# Vraag-antwoordsysteem op basis van dbpedia.org

# Input: id[tab]vraag
# Output: id[tab]antwoord[tab]antwoord[...]

# Jasper de Boer - s1889966
# Joel Coster - 
# Hans Rudolf Woldring -

import socket
import sys
import lxml
from lxml import etree

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

for line in sys.stdin:

    # hoe veel
    mod = []

    # wat we zoeken: eigenschap, lid etc
    x = []

    # van wie: de beatles etc.
    y = []
    
    [id,question] = line.rstrip().split("\t")

    xml = alpino_parse(question)

    print(id+" "+question)

    node = xml.xpath('//node[@cat="whq"]')
    if node:

        node = xml.xpath('//node[@rel="whd"]')
        if node:
            #print("Deze zin heeft een vraagwoord")

            node = xml.xpath('//node[@rel="whd" and @lemma]')
            if node:
                for child in node:
                    print("",end="")

                    if child.attrib["lemma"] == "wanneer":
                        
                        mod.append("wanneer")
                        
                        node = xml.xpath('//node[@rel="body"]/node[@rel="su"]/node[@lemma]')
                        if node:
                            for child in node:
                                y.append(((child.attrib["lemma"],child.attrib["frame"]),child.attrib["frame"]))

                        else:
                            node = xml.xpath('//node[@rel="body"]/node[@rel="su" and @lemma]')
                            if node:
                                for child in node:
                                    y.append((child.attrib["lemma"],child.attrib["frame"]))

                        node = xml.xpath('//node[@rel="hd" and @lemma]')
                        if node:
                            for child in node:
                                x.append((child.attrib["lemma"],child.attrib["frame"]))

                node = xml.xpath('//node[@cat="np" and @rel="su"]/node[@lemma]')
                if node:
                    for child in node:
                        x.append((child.attrib["lemma"],child.attrib["frame"]))

                    node = xml.xpath('//node[@cat="mwu" and @rel="obj1"]/node[@lemma]')
                    if node:
                        for child in node:
                            y.append((child.attrib["lemma"],child.attrib["frame"]))

                    else:
                        node = xml.xpath('//node[@rel="body"]/node[@rel="su"]/node[@rel="mod"]/node[@rel="obj1" and @lemma]')
                        if node:
                            for child in node:
                                y.append((child.attrib["lemma"],child.attrib["frame"]))
                        else:
                            node = xml.xpath('//node[@rel="body"]/node[@rel="su"]/node[@rel="mod"]/node[@rel="obj1"]/node[@rel="app"]/node[@lemma]')
                            if node:
                                for child in node:
                                    y.append((child.attrib["lemma"],child.attrib["frame"]))

                            else:
                                node = xml.xpath('//node[@rel="body"]/node[@rel="su"]/node[@rel="mod"]/node[@rel="obj1"]/node[@lemma]')
                                if node:
                                    for child in node:
                                        y.append((child.attrib["lemma"],child.attrib["frame"]))
    
            else:
                node = xml.xpath('//node[@cat="np" and @rel="whd"]/node[@cat="ap"]/node[@lemma]')
                if node:
                    
                    for child in node:
                        mod.append((child.attrib["lemma"],child.attrib["frame"]))

                    node = xml.xpath('//node[@cat="np" and @rel="whd"]/node[@rel="hd"]')
                    if node:
                        for child in node:
                            x.append((child.attrib["lemma"],child.attrib["frame"]))

                        node = xml.xpath('//node[@rel="body"]/node[@rel="su" and @lemma]')
                        if node:
                            for child in node:
                                y.append((child.attrib["lemma"],child.attrib["frame"]))

                        else:
                            node = xml.xpath('//node[@rel="body"]/node[@rel="obj1"]/node[@lemma]')
                            if node:
                                for child in node:
                                    y.append((child.attrib["lemma"],child.attrib["frame"]))

                else:
                    node = xml.xpath('//node[@rel="hd" and @lemma]')
                    if node:
                        for child in node:
                            x.append((child.attrib["lemma"],child.attrib["frame"]))

                        node = xml.xpath('//node[@rel="su"]/node[@lemma]')
                        if node:
                            for child in node:
                                y.append((child.attrib["lemma"],child.attrib["frame"]))
                                
                        else:
                            node = xml.xpath('//node[@rel="su" and @lemma]')
                            if node:
                                for child in node:
                                    y.append((child.attrib["lemma"],child.attrib["frame"]))
                            
        else:
            print("Dit is een andere vraagzin")
        
    else:
        print("Dit is geen vraag")

    print(mod)
    print(x)
    print(y)
