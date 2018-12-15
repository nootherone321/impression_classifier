from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

RP_url = "https://www.tabers.com/tabersonline/view/Tabers-Dictionary/767492/0/Medical_Abbreviations"
filename = "medical_abbreviations.csv"
f = open(filename, "w")

headers = "entry, definition\n"
f.write(headers)

uClient = uReq(RP_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("section",{"class":"section"})

for container in containers:

    # obtain remainder of scraped info by using findAll function
    entries = container.findAll("b")

    for e in entries:
        key = e.text.strip()
        if any(c.islower() for c in key):
            continue
        defin = e.next_sibling

        # start writing to CSV file
        f.write( "{},{}\n".format(key, defin) )
f.close()


import csv
dict_acronyms = {}
with open('medical_abbreviations.csv') as csv_acronyms:
    reader = csv.reader(csv_acronyms, delimiter=',', quotechar="|")
    next(reader,None) # skip headers
    for row in reader:
        dict_acronyms[row[0]] = row[1].strip()
dict_acronyms
