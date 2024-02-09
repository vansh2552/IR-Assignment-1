import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import re
import string
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
tokenizer = TweetTokenizer()
patterns = r"\b(?:[a-zA-Z](?:[a-zA-Z'_]*[a-zA-Z])?|(?<![_-])['_-](?![_-]))\b"

pickle_file_path = "positional_index.pkl"
with open(pickle_file_path, "rb") as file:
    positional_index = pickle.load(file)

def preprocess(query):
    lowercase_content = query.lower()
    tokens = re.findall(patterns, lowercase_content)
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [token for token in tokens if token not in string.punctuation]
    tokens = [token for token in tokens if token.strip()]
    return tokens

def phrase_query(positional_index, words):

    for word in words:
        if word not in positional_index:
            return []
    
    if len(words) == 1:
        return list(positional_index.get(words[0])[1].keys())

    # Initialize result set
    result = set()

    # Get the first word in the phrase
    first_word = words[0]

    # Get the posting list for the first word
    first_word_postings = positional_index.get(first_word, {})
    
    # Iterate through documents containing the first word
    for doc_id in first_word_postings[1]:
        # Check if other words in the phrase exist in the same document
        if all(doc_id in positional_index[word][1] for word in words[1:]):
            # Check if positions of subsequent words are in correct order
            first_word_positions = first_word_postings[1][doc_id]
            for position in first_word_positions:
                if all((position + i + 1) in positional_index[word][1][doc_id] for i, word in enumerate(words[1:])):
                    # If all positions are consecutive, include the document ID in the result
                    result.add(doc_id)
                    break  # Break the loop if one occurrence is found
    
    return list(result)

n = int(input())
for _ in range(n):
    query = input("Enter query "+str(_+1)+": ")
    query = preprocess(query)

    result = phrase_query(positional_index,query)

    print("Number of documents retrieved for query"+ str(_+1)+ "using positional index: "+str(len(result)))
    print("Names of documents retrieved for query"+str(_+1)+ "using positional index: ",end=" ")
    for i in result:
        print("file"+str(i)+".txt",end=" ")
    print()
    
    
    




    

    
