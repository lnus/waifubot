import requests, random
from bs4 import BeautifulSoup
base = "https://konachan.com/post?tags={}+order%3Arandom+rating:explicit"

def get_hentai(tags):
    href = None
    debug = 0
    images = []
    source = requests.get(base.format(tags)).text
    soup = BeautifulSoup(source, "html.parser")
    a = soup.find("a",{"class": "directlink"})
    try: 
        href = "http:" + a["href"]
        return("\n"+href)
    except: 
        return("\nNo images were found, sorry :(")
