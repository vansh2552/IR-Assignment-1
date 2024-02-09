import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import re
import string
import pickle
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
tokenizer = TweetTokenizer()
patterns = r"\b(?:[a-zA-Z](?:[a-zA-Z'_]*[a-zA-Z])?|(?<![_-])['_-](?![_-]))\b"

pickle_file_path = "unigram_inverted_index.pkl"
with open(pickle_file_path, "rb") as file:
    inverted_index = pickle.load(file)

def preprocess(query):
    lowercase_content = query.lower()
    tokens = re.findall(patterns, lowercase_content)
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [token for token in tokens if token not in string.punctuation]
    tokens = [token for token in tokens if token.strip()]
    return tokens

def execute(list1,list2,operation):
    result=[]
    all_docs = set(range(1, 1000))
    if operation == "AND":
        result = [item for item in list1 if item in list2]
    elif operation == "OR":
        result = list(set(list1 + list2))

    elif operation == "AND NOT":

        for item in list1:
            if item not in list2:
                result.append(item)
        
    elif operation == "OR NOT":
        for item in all_docs:
            if item not in list2 or item in list1:
                #print(item)
                result.append(item)
    

    return result


n = int(input())
for _ in range(1,n+1):
    query = input("Enter query: ")
    ops = input("Enter operations: ")

    query = preprocess(query)
    ops = ops.split(',')
    result=[]

    i=0
    while i < len(query):
        if i == 0:
            if query[i] not in inverted_index:
                doc1 = []
            else:
                doc1 = inverted_index[query[i]]

            if query[i+1] not in inverted_index:
                doc2 = []
            else:
                doc2 = inverted_index[query[i+1]]
            
            operator = ops[i]
            result = execute(doc1,doc2,operator)
            i = i + 1
        else:
            print(query[i])
            if query[i] not in inverted_index:
                doc = []
            else:
                doc = inverted_index[query[i]]
            operator = ops[i-1]
            result = execute(result,doc,operator)
        i+=1
            
    
    print("Query ",_,":",end=" ")
    for j in range(len(query)):
        if j == len(query) - 1:
            print(query[j])
        else:
            print(query[j]+" "+ops[j]+" ",end=" ")

    print("Number of documents retrieved for query ",_,":", len(result))
    print("Names of the documents retrieved for query",_,":",end=" ")
    for i in range(len(result)):
        print("file"+str(result[i])+".txt",end=" ")
    print()


    
