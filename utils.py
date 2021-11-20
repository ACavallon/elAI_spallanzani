# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:10:31 2021

@author: Abdou Rockikz
"""
import requests
import json
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

url_dom = 'https://eliaspallanzanivive.wordpress.com/'

internal_urls = set()
external_urls = set()

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


is_valid(url_dom)


def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    # all URLs of `url`
    urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    
    
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        
        href = urljoin(url, href)

        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        
        if not is_valid(href):
            # not a valid URL
            continue
        if href in internal_urls:
            # already in the set
            continue
        if domain_name not in href:
            # external link
            if href not in external_urls:
                print("External link: "+href)
                external_urls.add(href)
            continue
        
        print(href)
        urls.add(href)
        internal_urls.add(href)
    
    return urls


# number of urls visited so far will be stored here
total_urls_visited = 0

def crawl(url, max_urls=30):
    """
    Crawls a web page and extracts all links.
    You'll find all links in `external_urls` and `internal_urls` global set variables.
    params:
        max_urls (int): number of max urls to crawl, default is 30.
    """
    global total_urls_visited
    total_urls_visited += 1
    print(url)
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)


def process_crawl(url_dom):
    """
    The crawler is run on all the links of the URL.
    """
    crawl(url_dom)
    print("[+] Total Internal links:", len(internal_urls))
    print("[+] Total External links:", len(external_urls))
    print("[+] Total URLs:", len(external_urls) + len(internal_urls))

    list_internal_links = list(internal_urls)

    with open('list_pages.json', 'w', encoding='utf-8') as f:
        json.dump(list_internal_links, f, ensure_ascii=False, indent=4)



def extract_text(url_sub, list_drop):
    """
    Text extraction from a URL.
    """
    response =requests.get(url_sub)
    soup = BeautifulSoup(response.content, "html.parser")    

    dict_elements = {}
    cont = 0
    
    # Extraction of the p elements
    for i in soup.findAll('p'):
        dict_elements[cont] = i.text        
        cont +=1

    # Remove non significant elements
    list_blocks = [dict_elements[i] for i in dict_elements.keys() if ((len(dict_elements[i])>0) & ~(any(x in dict_elements[i] for x in list_drop)) & ~(dict_elements[i].isspace()))]    
    
    # Merging all text   
    final_text = ' '.join(list_blocks)    

    return final_text