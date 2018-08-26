import gensim
import sys



# Function that makes the word to vector model
def make_model(vec_file_path):
    google_vec_file = vec_file_path
    google_model = gensim.models.KeyedVectors.load_word2vec_format(google_vec_file, binary=True)
    return google_model

    

# Function to take a document as a list of words and return the document vector
def get_doc_vec(words, model):
    good_words = []
    for word in words:
        # Words not in the original model will fail
        try:
            if model.wv[word] is not None:
                good_words.append(word)
        except:
            continue
    # If no words are in the original model
    if len(good_words) == 0:
        return None
    # Return the mean of the vectors for all the good words
    return model.wv[good_words].mean(axis=0)