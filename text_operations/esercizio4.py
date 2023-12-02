import requests
import nltk
nltk.download('book')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from rake_nltk import Rake

# Text Acquisition

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
url1 = "https://www.nltk.org/book/ch06.html"
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



#####ESERCIZIO 4######

#document example **test**

document = """
And first with regard to Emigration. It must not be supposed that
Americaâ€”and for the present let us confine our attention to the
United Statesâ€”welcomes without exception the human stream. There are
undoubtedly elements in it which would be objectionable anywhere. There
are hordes of paupers and loafers and neâ€™erdoweels, who are as little
likely to do any good for themselves, or to benefit the community, in
the New World as in the Old. But apart from these, there has been a
flow of shrewd workers and skilled artisans, which a certain section
of the American nation is disposed to regard with a sour look. The
reason is not far to seek. The dominant economic policy of America has
been, as we know, one of strict protection of their own industries.
For the benefit of the few, the many are heavily burdened, in the
beliefâ€”fallacious, and not always genuinely entertainedâ€”that in process
of time the many will reap the harvest. The conductors of these
domestic industries are glad enough to get all the experienced foreign
labour they can; but the domestic labourer says, very naturally, that
the importation is unjust to him. He says, in effect: â€˜You tax foreign
products to shut out competition with yourselves; but you admit freely
foreign producers to compete with me. You raise the cost of living to
me by the imposition of taxes to foster your trades; yet you reduce
my means of living by suffering immigration which tends to reduce
the level of wages.â€™ Here is friction, and friction which is already
producing sparks. It is not difficult to foresee the result. The
working-classes cannot continue to burn the candle at both ends for
ever. It is not practicable for any country in these days to prohibit,
or even to restrict, the importation of human beings. Nor can America
say:˜We will receive any number of farm-labourers, or miners, or
anybody disposed to squat in the backwoods and open up our country; but
we will draw the line at mechanics or any form of skilled labour which
we can ourselves produce to the extent of our requirements.â€™ The effect
of the supply of foreign labour would have been more apparent ere
this but for the suicidal policy of the American trades-unions, which
practically prohibit the evolution of domestic skill, by forbidding
apprenticeship to crafts. But, nevertheless, the effect must eventually
be to diminish the reward of labour.
"""
r = Rake()

r.extract_keywords_from_text(document)

ranked_keywords = r.get_ranked_phrases()

for keyword in ranked_keywords:
    print("keywords:", keyword)