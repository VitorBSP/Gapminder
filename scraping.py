#%%
import urllib as urlr
from bs4 import BeautifulSoup
import numpy as np

req = urlr.request.Request('https://www.sport-histoire.fr/en/Geography/Countries_by_alphabetical_order.php', 
                            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
html = urlr.request.urlopen(req)
bs = BeautifulSoup(html, 'html.parser')

#%%
bs.find_all('thead')
paises = bs.find_all('tr')
paises.pop(0)

#%%
nome_pais = []
continente = []
capital = []
for information in paises:
    pais = information.get_text(separator='\n').splitlines()
    nome_pais.append(pais[0])
    capital.append(pais[1])
    continente.append(pais[2])