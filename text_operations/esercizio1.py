import requests
import nltk
nltk.download('book')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Text Acquisition

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
url1 = "https://www.gutenberg.org/files/2554/2554-0.txt"
response = requests.get(url1)
text = response.text
print(text)

# Pre-processing

tokens = nltk.word_tokenize(text)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)

tokens2 = set()
for t in tokens:
    if not t in stopwords.words('english'):
        tt = nltk.pos_tag([t])
        print(tt)
        if tt[0][1][0:2] == 'NN':
            tokens2.add(t)
print("tokens without stopwords and with nouns selection:")
print(tokens2)

# Stemming

porter = PorterStemmer()
for t in tokens2:
    print(porter.stem(t))