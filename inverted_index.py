import pickle


inverted_index = {}
doc_id = 1
for i in range(1,1000):
    file_path = 'pre-processed_files/file'+str(i)+".txt"
    
    with open(file_path, 'r') as file:
        doc = file.read()
        tokens = doc.split()
        
        for token in tokens:
            
            if token not in inverted_index:
                inverted_index[token] = []
            if doc_id not in inverted_index[token]:
                inverted_index[token].append(doc_id)
    doc_id += 1

# for term, doc_ids in inverted_index.items():
#     print(f"{term}: {doc_ids}")

def save_index_to_file(index, filename):
    with open(filename, 'wb') as file:
        pickle.dump(index, file)


save_index_to_file(inverted_index, 'unigram_inverted_index.pkl')

