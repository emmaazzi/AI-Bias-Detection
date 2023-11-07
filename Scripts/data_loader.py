# data_loader.py
import json
import pandas as pd
from glob import glob
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# You might need to download these resources if you haven't already
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stopwords and lemmatize the words
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stopwords.words('english')]
    # Join the tokens back into a string
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text


def load_data(json_folder_path, limit=None):
    # Create a list to hold the JSON data
    data_list = []

    # Use glob to match the json file pattern
    json_files = glob(json_folder_path + '/*.json')

    # If a limit is specified, slice the list of json files
    if limit is not None:
        json_files = json_files[:limit]

    for file_name in json_files:
        with open(file_name, 'r') as file:
            # Load the content of the JSON file and add it to the list
            data_list.append(json.load(file))

    # Convert the list of dictionaries to a pandas DataFrame
    data_frame = pd.DataFrame(data_list)

    # Preprocessing step
    data_frame['content_preprocessed'] = data_frame['content'].apply(preprocess_text)

    return data_frame


# If you have other preprocessing functions, define them here
