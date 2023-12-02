from rake_nltk import Rake

# Sample text document
document = """
Natural Language Processing (NLP) is a subfield of artificial intelligence 
that focuses on the interaction between computers and humans through natural 
language. NLP techniques are used for various applications, including 
text summarization, sentiment analysis, and keyword extraction.
"""

# Create a Rake object
r = Rake()

# Extract keywords
r.extract_keywords_from_text(document)

# Get ranked keywords
ranked_keywords = r.get_ranked_phrases()

# Print the ranked keywords
for keyword in ranked_keywords:
    print(keyword)