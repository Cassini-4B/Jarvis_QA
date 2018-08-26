# Jarvis_QA

This is my attempt at building a closed-domain, retrieval-based question answering machine.  I took the 'All the News' dataset from Kaggle, which consists of ~150,000 news articles that were scraped from a variety of American news outlets from 2016-2017:  
https://www.kaggle.com/snapcrack/all-the-news

I cleaned the dataset by removing punctuation, special charaters, extra spaces, numbers and stopwords, and then lowercased tokenized, and stemmed the remaining text.  I then used a Count Vectorizer and fit the text into a LDA (latent dirichlet allocation) model to extract topics from the dataset.

I also used Google's Word2Vec to get document vectors for each article, then used that to cluster using kMeans.  I also used these vectors to find the most relevant article to an input query by applying sklearn's nearest neighbor algorithm.

### Jarvis speaks!  
![alt text](https://raw.githubusercontent.com/username/projectname/branch/path/to/jarvis_flask.png)

Here's my Jarvis interface.  You input text about an article or topic you've read, and when you click on 'House Party Protocol', you get a random choice of 3 (out of 10) relevant articles as a response to your input query, and I've tied it to marytts (http://mary.dfki.de/) to synthesize a voice output.  
