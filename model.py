import pickle
import os

# Directory containing the extracted model data
extracted_model_folder = 'extracted_model'

# Collect all files within the directory
files_to_pickle = []
for root, dirs, files in os.walk(extracted_model_folder):
    for file in files:
        file_path = os.path.join(root, file)
        files_to_pickle.append(file_path)

# Pickle the list of file paths
output_pickle_file = 'extracted_model.pkl'
with open(output_pickle_file, 'wb') as f:
    pickle.dump(files_to_pickle, f)
