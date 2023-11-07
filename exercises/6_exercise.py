from collections import Counter
import string
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk import ngrams
from nltk import BigramAssocMeasures, BigramCollocationFinder
from nltk.text import Text 
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np 
import spacy
import eng_spacysentiment

# download the list of stop words (in english) 
# only the 1st you run the code
nltk.download('stopwords')

# create sets of punctuation marks and stop words
stop_words = set(stopwords.words('english')) 
excluded_punct = set(string.punctuation)

# open the file with the text corpus  
f = open("6_led.txt", "r")
orig_text = f.read()

# lowercase
text = orig_text.lower()

# tokenization
words = word_tokenize(text)
print(words[:20])

# clean tokens from punctuation and stop words
clean_text = [w for w in words if w not in excluded_punct and w not in stop_words]
print(clean_text[:20])

# word frequency with Counter
freq = Counter(clean_text).most_common(20)
print(freq)

# word frequency with FreqDist 
fdist1 = FreqDist(clean_text).most_common(20)
print(fdist1)

# get bigrams and calculate frequency of bigrams
n_grams = ngrams(clean_text, 2)
fdist3 = FreqDist(n_grams).most_common(20)
print(fdist3)

# initialize collocation measures for bigrams
bigrams = nltk.collocations.BigramAssocMeasures()

# find bigrams in the corpus
finder = BigramCollocationFinder.from_words(clean_text)
finder.apply_freq_filter(3)

# score bigrams w/ Chi-squared
print("chi-squared")
scored_chi = finder.score_ngrams(bigrams.chi_sq)
for bigram, score in scored_chi [:5]:
    print(bigram, score)
print(finder.nbest(bigrams.chi_sq, 10))

# PMI score 
print("PMI")
scored_pmi = finder.score_ngrams(bigrams.pmi)
for bigram, score in scored_pmi[:5]:
    print(bigram, score)

print(finder.nbest(bigrams.pmi, 10))

# concordance
tokens_to_be_analysed = Text(words)
tokens_to_be_analysed.concordance("military", 40, 20)

# TF-IDF
# split the corpus 
texts = [t for t in text.split('\n\n') if t and len(t) > 1]
print(len(texts))

# Initialize a TFIDF object, applying some settings
tfidf = TfidfVectorizer(analyzer='word', sublinear_tf=True, max_features=500, tokenizer=word_tokenize)
tdidf = tfidf.fit(texts)

# Get the terms with the highest IDF score
inds = np.argsort(tfidf.idf_)[::-1][:10]
top_IDF_tokens = [list(tfidf.vocabulary_)[ind] for ind in inds]

print(top_IDF_tokens)

# NER

# download the model for English
nlp = spacy.load("en_core_web_sm")

doc = nlp(orig_text)
print([(X.text, X.label_) for X in doc.ents])

# Sentiment 

nlp2 = eng_spacysentiment.load()
doc2 = nlp2(texts[0]) # apply it to the first text in the corpus
print(doc2.cats)