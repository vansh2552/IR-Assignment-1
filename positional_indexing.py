import pickle

positional_index={}           # { word: [freq, {fileNo.:[positionNo] } ]}

for i in range(1,1000):
    file_path = "pre-processed_files/file"+str(i)+".txt" 
    with open(file_path, 'r') as file:
        tokens = file.read()
        tokens = tokens.split(" ")
        
        for j in range(len(tokens)):
            if tokens[j] not in positional_index:
                positional_index[tokens[j]] = [1,{i:[j+1]}]
            else:
                frequency = positional_index[tokens[j]][0]
                docIDs = positional_index[tokens[j]][1]

                if i not in docIDs:
                    docIDs[i] = [j+1]
                    frequency += 1
                else:
                    positions = docIDs[i]
                    positions.append(j+1)
                    docIDs[i] = positions
                
                positional_index[tokens[j]] = [frequency,docIDs]


def save_index_to_file(index, filename):
    with open(filename, 'wb') as file:
        pickle.dump(index, file)


save_index_to_file(positional_index, 'positional_index.pkl')

