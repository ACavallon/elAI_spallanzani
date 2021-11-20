# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 09:59:36 2021

@author: acava
"""

# import library
import requests
import time
import re
import os
import json
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

import utils as F

url_dom = 'https://eliaspallanzanivive.wordpress.com/'
url_sub = 'https://eliaspallanzanivive.wordpress.com/2021/11/06/dispalcature/'

if(not(os.path.exists('list_pages.json'))):
   F.process_crawl(url_dom)
    
with open('list_pages.json') as f:
    list_url = json.load(f)
    

list_url_sub = list_url[0:5]


list_drop = ["Inserisci i tuoi dati qui sotto o clicca su un'icona", "Stai commentando usando il tuo account", "Notificami nuovi commenti via e-mail", "Connessione a %s...", "Notificami nuovi commenti via e-mail", "Mandami una notifica per nuovi articoli via e-mail", "Questo sito utilizza Akismet per ridurre lo spam. Scopri come vengono elaborati i dati derivati dai commenti.", "Δ"]

dict_final = []
count = 0

for u in list_url_sub:
    print(count)
    dict_final[count] = F.extract_text(
        url_sub = u
        )
    count += 1