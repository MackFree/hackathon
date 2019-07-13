#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs

WEBSITE="https://www.webelements.com/hydrogen/"
ELEMENTS = []
WHITELIST = set(["hydrogen", "helium", "lithium", "beryllium", "boron", "carbon",
        "nitrogen", "oxygen", "fluorine", "neon", "sodium", "magnesium", "aluminium",
        "silicon", "phosphorus", "sulfur", "chlorine", "argon", "potassium", "calcium"])

req = requests.get(WEBSITE)
soup = bs(req.text, "html.parser")
for link in soup.find_all('a'):
    link_href = link.get("href")
    if link_href.startswith("..") and link_href.endswith("/") and not link_href.startswith("../periodicity"):
        element_name = link_href.split("/")[1]
        #print(element_name)
        ELEMENTS.append(element_name)


for element in ELEMENTS:
    f = open("elements/" + element + ".txt", 'w')
    if element not in WHITELIST:
        continue
    req = requests.get("https://www.webelements.com/{}/compounds.html".format(element))
    soup = bs(req.text, "html.parser")
    for link in soup.find_all('li'):
        name = link.text
        if ":" in name and not "Abundance" in name:
            f.write(name + "\n")
    f.close()

