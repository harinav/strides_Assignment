from nltk import word_tokenize
from nltk.corpus import stopwords
import numpy as np
from gensim.models import Word2Vec
import gensim.models.keyedvectors as word2vec
import gzip
import timeline

def document_vector(word2vec_model, doc):
    		doc =[word for word in doc if word in word2vec_model.vocab]
    		return np.mean(word2vec_model[doc], axis=0)

stop_words = stopwords.words('english')
def preprocess(text):
    		text = text.lower()
    		doc = word_tokenize(text)
    		doc = [word for word in doc if word not in stop_words]
    		doc = [word for word in doc if word.isalpha()]
    		return doc

def main():
	texts=timeline.timeline()
	corpus = [preprocess(text) for text in texts]
	filename = '/home/sys3002/Desktop/GoogleNews-vectors-negative300.bin.gz'
	word2vec_model = word2vec.KeyedVectors.load_word2vec_format(filename, binary=True)
	for doc in corpus:
    		print document_vector(word2vec_model, doc) 

if __name__ == '__main__':
    main()


