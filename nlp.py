# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:02:23 2021

@author: acava
"""

import re
from nltk.stem import WordNetLemmatizer

def remove_punctuation(words):
    """
    Remove punctuation from list of tokenized words
    """
    
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
            
    return new_words


def lemmatize_verbs(words):
    """
    Lemmatize verbs in list of tokenized words
    """
    
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
        
    return lemmas