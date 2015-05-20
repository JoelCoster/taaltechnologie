# Eindopdracht Taaltechnologie
# Vraag-antwoordsysteem op basis van dbpedia.org

# Input: id[tab]vraag
# Output: id[tab]antwoord[tab]antwoord[...]

# Jasper de Boer - s1889966
# Joel Coster - s2555255

import socket
import sys
import lxml
from lxml import etree
from support_functions import *
from SPARQLWrapper import SPARQLWrapper, JSON

for line in sys.stdin:

    # hoe veel
    mod = []

    # wat we zoeken: eigenschap, lid etc
    x = []

    # van wie: the beatles etc.
    y = []
    
    [id,question] = line.rstrip().split("\t")

    # Gebiedende wijs "Geef de.." "Noem de..."
    qList = question.split(" ")
    gebiedendeWijs = ["geef","noem"]
    if qList[0].lower() in gebiedendeWijs:
        qList[0] = "Wat is

    xml = alpino_parse(question)

    print(id+"\t"+question)

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
                                y.append(child.attrib["lemma"])

                        else:
                            node = xml.xpath('//node[@rel="body"]/node[@rel="su" and @lemma]')
                            if node:
                                for child in node:
                                    y.append(child.attrib["lemma"])

                        node = xml.xpath('//node[@rel="hd" and @lemma and not(@rel="det")]')
                        if node:
                            for child in node:
                                x.append(child.attrib["lemma"])

                node = xml.xpath('//node[@cat="np" and @rel="su"]/node[@lemma and not(@rel="det")]')
                if node:
                    for child in node:
                        x.append(child.attrib["lemma"])

                    node = xml.xpath('//node[@cat="mwu" and @rel="obj1"]/node[@lemma and not(@rel="det")]')
                    if node:
                        for child in node:
                            y.append(child.attrib["lemma"])

                    else:
                        node = xml.xpath('//node[@rel="body"]/node[@rel="su"]/node[@rel="mod"]/node[@rel="obj1" and @lemma and not(@rel="det")]')
                        if node:
                            for child in node:
                                y.append(child.attrib["lemma"])
                        else:
                            node = xml.xpath('//node[@rel="body"]/node[@rel="su"]/node[@rel="mod"]/node[@rel="obj1"]/node[@rel="app"]/node[@lemma]')
                            if node:
                                for child in node:
                                    y.append(child.attrib["lemma"])

                            else:
                                node = xml.xpath('//node[@rel="body"]/node[@rel="su"]/node[@rel="mod"]/node[@rel="obj1"]/node[@lemma]')
                                if node:
                                    for child in node:
                                        y.append(child.attrib["lemma"])

                else:
                    node = xml.xpath('//node[@rel="obj1"]/node["@lemma" and @rel="mwp"]')
                    if node:
                        for child in node:
                            y.append(child.attrib["lemma"])

                        node = xml.xpath('//node[@rel="vc"]/node[@rel="hd" and @lemma]')
                        if node:
                            for child in node:
                                x.append(child.attrib["lemma"])

                        else:
                            node = xml.xpath('//node[@rel="body"]/node[@rel="hd" and @lemma]')
                            if node:
                                for child in node:
                                    x.append(child.attrib["lemma"])
                    else:
                        node = xml.xpath('//node[@rel="obj1"]/node[@rel="app"]/node[@rel="mwp" and @lemma]')
                        if node:
                            for child in node:
                                y.append(child.attrib["lemma"])

                            node = xml.xpath('//node[@rel="body"]/node[@rel="vc"]/node[@rel="hd" and @lemma]')
                            if node:
                                for child in node:
                                    x.append(child.attrib["lemma"])
                            else:
                                node = xml.xpath('//node[@rel="body"]/node[@rel="hd" and @lemma]')
                                if node:
                                    for child in node:
                                        x.append(child.attrib["lemma"])

                        else:
                            node = xml.xpath('//node[@rel="body"]/node[@rel="obj1" and @lemma]')
                            if node:
                                for child in node:
                                    y.append(child.attrib["lemma"])

                                node = xml.xpath('//node[@rel="body"]/node[@rel="hd" and @lemma]')
                                if node:
                                    for child in node:
                                        x.append(child.attrib["lemma"])
                            else:
                                node = xml.xpath('//node[@rel="body"]/node[@rel="vc"]/node[@rel="hd" and @lemma]')
                                if node:
                                    for child in node:
                                        x.append(child.attrib["lemma"])
                                        
                                    node = xml.xpath('//node[@rel="body"]/node[@rel="vc"]/node[@rel="obj1" and @lemma]')
                                    if node:
                                        for child in node:
                                            y.append(child.attrib["lemma"])

                                
            else:
                
                node = xml.xpath('//node[@cat="np" and @rel="whd"]/node[@cat="ap"]/node[@lemma]')
                if node:
                    
                    for child in node:
                        mod.append(child.attrib["lemma"])

                    node = xml.xpath('//node[@cat="np" and @rel="whd"]/node[@rel="hd" and not(@rel="det")]')
                    if node:
                        for child in node:
                            x.append(child.attrib["lemma"])

                        node = xml.xpath('//node[@rel="body"]/node[@rel="su" and @lemma]')
                        if node:
                            for child in node:
                                y.append(child.attrib["lemma"])

                        else:
                            node = xml.xpath('//node[@rel="body"]/node[@rel="obj1"]/node[@lemma]')
                            if node:
                                for child in node:
                                    y.append(child.attrib["lemma"])

                else:

                    node = xml.xpath('//node[@rel="body"]/node[@rel="vc"]/node[@rel="hd" and @lemma]')
                    if node:
                        for child in node:
                            x.append(child.attrib["lemma"])

                        node = xml.xpath('//node[@rel="body"]/node[@rel="su"]/node[@rel="app"]/node[@lemma]')
                        if node:
                            for child in node:
                                y.append(child.attrib["lemma"])

                        else:
                            node = xml.xpath('//node[@rel="body"]/node[@rel="su"]/node[@rel="app" and @lemma]')
                            if node:
                                for child in node:
                                    y.append(child.attrib["lemma"])

                            else:
                                node = xml.xpath('//node[@rel="body"]/node[@rel="su" and @lemma]')
                                if node:
                                    for child in node:
                                        y.append(child.attrib["lemma"])

                        
                    else:
                        node = xml.xpath('//node[@rel="hd" and @lemma and not(@rel="det")]')
                        if node:
                            for child in node:
                                x.append(child.attrib["lemma"])

                            node = xml.xpath('//node[@rel="su"]/node[@lemma]')
                            if node:
                                for child in node:
                                    y.append(child.attrib["lemma"])
                                    
                            else:
                                node = xml.xpath('//node[@rel="su" and @lemma]')
                                if node:
                                    for child in node:
                                        y.append(child.attrib["lemma"])
                            
        else:
            print("Dit is een andere vraagzin")
        
    else:
        print("Dit is geen vraag")

    prop = []
    blacklist = ["zijn","in","jaar","van","op","door"]
    
    for word in x:
        if word in blacklist: pass
        else:
            prop.append(word)

    property = getProperty(prop)

    print("Prop:" +str(prop))
    print("Y: "+str(y))

    if property != "":

        page = searchPage(y)

        if str(page) != "None":

            query = makeQuery(property,page,mod)

            results = answerQuestion(query)
            print(id,end="")
            for result in results["results"]["bindings"]:
                for arg in result:
                    print("\t"+result[arg]["value"],end="")
            print()
        
    else:
        print("Antwoord vinden lukt nog niet")
        
