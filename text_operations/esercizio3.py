# Write a Python algorithm that given a query expressed as
# a set of words, expands the input query by adding all (or
# some) word synonyms

import nltk
from nltk.corpus import wordnet as wn
nltk.download('wordnet')

def get_synonyms(word):
    synonyms = set()
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def expand_query_with_synonyms(query):
    expanded_query = set()

    for word in query:
        synonyms = get_synonyms(word)
        if synonyms:
            expanded_query.add(word)
            expanded_query.update(synonyms)
    return list(expanded_query)

#example 

input_query = ["flower", "mouse"]
expanded_query = expand_query_with_synonyms(input_query)

print("Original Query:", input_query)
print("Expanded Query:", expanded_query) 