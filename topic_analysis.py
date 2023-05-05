
import nltk
import gensim
import pandas as pd

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

from gensim.corpora import Dictionary, MmCorpus
from gensim.models import LdaModel

import string

def preprocess_text(text):
    # Tokenize text
    tokens = word_tokenize(text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.lower() not in stop_words and token not in string.punctuation]
    
    # Stem words
    stemmer = SnowballStemmer('english')
    tokens = [stemmer.stem(token) for token in tokens]
    
    return tokens

nltk.download('stopwords')
nltk.download('punkt')

df = pd.read_csv('china_articles_analyzed.csv')
df['processed_article'] = df['article'].apply(preprocess_text)

# Create dictionary of preprocessed text
dictionary = Dictionary(df['processed_article'])

dictionary.save('dictionary.gensim')

# Create corpus of preprocessed text
corpus = [dictionary.doc2bow(text) for text in df['processed_article']]
MmCorpus.serialize('corpus.mm', corpus)

# Train LDA model on corpus
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5)

# Infer topic distribution for each article
df['topic_distribution'] = df['processed_article'].apply(lambda x: lda_model[dictionary.doc2bow(x)])

lda_model.save('lda_model.sav')
df.to_csv('china_articles_topic_modeled.csv')