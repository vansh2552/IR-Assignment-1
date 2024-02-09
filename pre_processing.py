import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
import string
import os
import re

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
tokenizer = TweetTokenizer()

def custom_tokenizer(text):
    patterns = r"\b(?:[a-zA-Z](?:[a-zA-Z'_]*[a-zA-Z])?|(?<![_-])['_-](?![_-]))\b"
    tokens = re.findall(patterns, text)
    return tokens

for i in range(1,1000):
    file_path = "text_files/file"+str(i)+".txt" 
    print("pre processing file ",i)
    with open(file_path, 'r') as file:
        file_content = file.read()

        if i < 6:
            print("original text for file ",str(i))
            print(file_content)


        lowercase_content = file_content.lower()
        if i < 6:
            print("Lowercase text for file ",str(i))
            print(lowercase_content)

        #tokens = tokenizer.tokenize(lowercase_content)
        tokens = custom_tokenizer(lowercase_content)
        if i < 6:
            print("Performing tokenization for file ",str(i))
            print(tokens)

        tokens = [word for word in tokens if word not in stop_words]
        if i < 6:
            print("Removing stopwords for file ",str(i))
            print(tokens)

        tokens = [token for token in tokens if token not in string.punctuation]
        if i < 6:
            print("Removing punctuations for file ",str(i))
            print(tokens)

        tokens = [token for token in tokens if token.strip()]
        if i < 6:
            print("Removing blank spaces for file ",str(i))
            print(tokens)
    
        pre_processed_path = "pre-processed_files/file"+str(i)+".txt" 
        os.makedirs(os.path.dirname(pre_processed_path), exist_ok=True)

        with open(pre_processed_path, 'w') as file:
            
        # Write the content to the file
            for item in tokens:
                item = item+" "
                file.write(item)


        


        
