""" This script removes punctuation, double spaces, special characters, numbers, stopwords, 
and it lowercases and stems text. """



import numpy as np
import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import porter


stemmer = porter.PorterStemmer()

stopwords = stopwords.words()




def cleaning(text):
    cleaned_text = []
    text1 = re.sub('—', '', text)  # remove dashes --
    text2 = re.sub('  ', ' ', text1)  # remove double spaces
    text3 = re.sub('[%s]' % re.escape(string.punctuation), ' ',text2)  # remove punctuation
    text4 = re.sub("’[a-z]*",'', text3)  # remove apostrophe s
    text5 = re.sub('[0-9]','',text4) # remove numbers
    text6 = re.sub('\“*\”*', '', text5.lower()) # remove quotation marks
    
    for t in text6.split(' '):
        if len(t)>2:
            if t not in stopwords:
                stem_word = stemmer.stem(t)
                if len(stem_word)>2:
                    cleaned_text.append(stem_word)
            
    return cleaned_text