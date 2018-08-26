#This script vectorizes cleaned, tokenized words to fit into LDA for topic modeling.


import numpy as np
import sys
import re
import pickle
import nltk


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation





def get_topics(text, model, num_components, n_top_words):
    cv = CountVectorizer(lowercase=False, input='content', stop_words='english', max_df=0.4,min_df=0.1,  
                     token_pattern='[a-z]{3,}')
    cv.fit(text)
    
    topic_model = model(n_components=num_components)
    vec_file = cv.transform([text])
    topic_model.fit(vec_file)
    feature_names = cv.get_feature_names()
    
    return(topic_model, feature_names, n_top_words)