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

data_path = 'data/'
url_dom = 'https://eliaspallanzanivive.wordpress.com/'
url_sub = 'https://eliaspallanzanivive.wordpress.com/2021/11/06/dispalcature/'

if(not(os.path.exists(os.path.join(data_path,'list_pages.json')))):
   F.process_crawl(url_dom)
    
with open('list_pages.json') as f:
    list_url = json.load(f)

list_drop = ["Inserisci i tuoi dati qui sotto o clicca su un'icona", "Stai commentando usando il tuo account", "Notificami nuovi commenti via e-mail", "Connessione a %s...", "Notificami nuovi commenti via e-mail", "Mandami una notifica per nuovi articoli via e-mail", "Questo sito utilizza Akismet per ridurre lo spam. Scopri come vengono elaborati i dati derivati dai commenti.", "Δ"]

dict_data = {}
count = 0

for u in list_url:
    print(count)
    dict_data[count] = {
        'name' : u,
        'text' : F.extract_text(
        url_sub = u,
        list_drop = list_drop
        )}
    count += 1
    
with open(os.path.join(data_path,'dict_data.json'), 'w') as f:
    json.dump(dict_data, f)