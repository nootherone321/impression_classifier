from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

RP_url = "https://radiopaedia.org/encyclopaedia/all/all?page="
filename = "radiopaedia_articles.csv"
#f = open(filename, "w")

#headers = "article_title, url, \n"
#f.write(headers)

uClient = uReq(RP_url + "1")
page_html = uClient.read()
uClient.close()

spage_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("a",{"class":"search-result-article"})

for container in containers:
    url = container["href"]
    title_container = container.findAll("h4",{"class":"search-result-title-text"})
    title = title_container[0].text
    print(title)