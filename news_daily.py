import requests
import urllib.request
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

DOMAIN = "https://thehackernews.com/"

def buscar_news(url):
   try:
      resposta = requests.get(url)
      if resposta.status_code == 200:
         return resposta.text
      else:
         print("Erro ao fazer requisição.")
         
   except Exception as error:
      print("Error: ", error)
      
      
def parsing(resposta_html):
   try:
      soup = BeautifulSoup(resposta_html, 'html.parser')
      return soup
   except Exception as error:
      print

def encontrar_links(soup):
   cards_pai = soup.find("div", class_="main-box clear")
   cards = cards_pai.find_all("a")
   links = []
   for card in cards:
      link = card["href"]
      links.append(link)
   return links
   
busca_resposta = buscar_news(DOMAIN)
if busca_resposta:
   soup_busca = parsing(busca_resposta)
   if soup_busca:
      links = encontrar_links(soup_busca)
      resposta_anuncio = buscar_news(DOMAIN + links[0])
      if resposta_anuncio:
         soup_anuncio = parsing(resposta_anuncio)
         print(soup_anuncio.prettify())
         session = requests.Session()
         retry = Retry(connect=3, backoff_factor=0.5)
         adapter = HTTPAdapter(max_retries=retry)
         session.mount('https://thehackernews.com/', adapter)
         session.mount('https://thehackernews.com/', adapter)

         session.get(DOMAIN)