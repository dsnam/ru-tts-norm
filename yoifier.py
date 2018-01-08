# -*- coding: utf-8 -*-
"""
Simple class to attempt to yoify a word that may have had the ё omitted. 
Currently does not attempt to use any context to correct the author and will
simply not modify the word if it is valid with no ё. This likely will not 
completely resolve ambiguity like все vs всё at the moment.

Needs a dictionary file. One is provided in data/.
@author: Alexander Dodson
"""

import re
import pandas as pd

class Yoifier:
    def __init__(self, dict_path='data/dict_transformed.txt'):
        self.words = set(pd.read_csv(dict_path, header=None)[0])
        self.ye_pat = re.compile('Е')
        self.yo_pat = re.compile('Ё')
        
    def yoify(self, word):
        word_up = word.upper()
        yo_match = re.search(self.yo_pat, word_up)
        ye_match = re.search(self.ye_pat, word_up)
        if yo_match or not ye_match or word_up in self.words:
            return word
        for match in self.ye_pat.finditer(word_up):
            word_yo = word_up[:match.start()] + 'Ё' + word_up[(match.start()+1):]
            if word_yo in self.words:
                return word[:match.start()]+ 'ё' + word[(match.start()+1):]