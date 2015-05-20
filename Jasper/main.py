# Eindopdracht Taaltechnologie
# Vraag-antwoordsysteem op basis van dbpedia.org

# Input: id[tab]vraag
# Output: id[tab]antwoord[tab]antwoord[...]

# Jasper de Boer - s1889966
# Joel Coster - s2555255

import sys
import lxml
from lxml import etree
from support_functions import *

for line in sys.stdin:

    mod = []
    x = []
    y = []
    
    [id,question] = line.rstrip().split("\t")

    print(id,end="")

    xml = alpino_parse(question)

    node = xml.xpath('//node[@cat="whq"]')
    if node:

        node = xml.xpath('//node[@rel="whd"]')
        if node:

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

    prop = []
    blacklist = ["zijn","in","jaar","van","op","door"]
    
    for word in x:
        if word in blacklist: pass
        else:
            prop.append(word) 

    modList = {"lang": ["DESC","dbpedia-owl:playingTime"],
               "kort": ["ASC", "dbpedia-owl:playingTime"],
               "eerste": ["ASC", "prop-nl:releasedatum "],
               "laat": ["DESC","prop-nl:releasedatum"],
               "nieuw": ["DESC","prop-nl:releasedatum"]}

    order = ""
    if len(prop) > 0:
        if prop[0] in modList:
            order = modList[prop[0]]
            prop = prop[1:]

    property = getProperty(prop)
    page = "None"

    if property != "":
        page = searchPage(y)

    if str(page) == "None":
        page = "_".join(y)

    if str(page) != "None" and property != "":

        query = makeQuery(property,page,mod,order)
        results = answerQuestion(query)

        for result in results["results"]["bindings"]:
            for arg in result:
                print("\t"+result[arg]["value"],end="")

    else:
        print("\t",end="")

    print()
