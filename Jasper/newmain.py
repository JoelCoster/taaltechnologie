import socket
import sys
import lxml
from lxml import etree
from SPARQLWrapper import SPARQLWrapper, JSON
from searchpage import *
from support_functions import *

debug = True

#[mod,x,y]
xpath = [
    ['//node[@rel="whd" and @lemma]','//node[@rel="body"]/node[@rel="su"]/node[@lemma]','//node[@rel="hd" and @lemma and not(@rel="det")]'],
    ['//node[@rel="whd" and @lemma]','//node[@rel="body"]/node[@rel="su" and @lemma]''//node[@rel="hd" and @lemma and not(@rel="det")]']
    ]
    

for line in sys.stdin:

    mod = []
    x = []
    y = []
    
    [id,question] = line.rstrip().split("\t")

    xml = alpino_parse(question)

    if debug:
        print(id+" "+question)

    node = xml.xpath('//node[@cat="whq"]')
    if node:
        for query in xpath:
            
            # mod
            node = xml.xpath(query[0])
            if node:
                for child in node:
                    mod.append(child.attrib["lemma"])
                    
                    # x
                    node = xml.xpath(query[1])
                    if node:
                        for child in node:
                            if "rel" in child.attrib:
                                if child.attrib["rel"] != "det":
                                    x.append(child.attrib["lemma"])

                        if len(x) > 0:

                            print(x)

                            # y    
                            node = xml.xpath(query[2])
                            if node:
                                for child in node:
                                    y.append(child.attrib["lemma"])

                                print(y)
                            else:
                                mod = []
                                x = []
                                y = []

                        else:
                            break
                            
                    else:
                        mod = []
                        x = []
                        y = []
                    

    else:
        print("Dit is geen vraag. Is het gebiedende wijs?")
