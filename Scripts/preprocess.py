import re
from bs4 import BeautifulSoup
from sklearn.model_selection import train_test_split

# Assuming _stopwords is a list of stopwords
_stopwords = [...]  # Load or define your list of Macedonian stopwords

def clean(text):
    # Parse the HTML content and get the text
    text = BeautifulSoup(text, "html.parser").get_text() 
    # Replace specified punctuation and symbols with space
    text = re.sub(r'[\|\|\"\'\-„“]', ' ', text)   
    # Convert text to lowercase
    text = text.lower()   
    return text

def tokenize(text):
    return text.split()

def remove_stopwords(tokens):
    return ' '.join(word for word in tokens if word not in _stopwords)

# Split the data into train and test sets
# train, test = train_test_split(df, test_size=0.2)
