import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Function to preprocess and clean the text
def preprocess_text(text):
    # Removing URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)

    # Converting to lowercase
    text = text.lower()

    # Removing numbers and punctuation
    text = re.sub(r"[^a-zA-Z]", ' ', text)

    # Tokenizing the text
    tokens = word_tokenize(text)

    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Joining the tokens back into a single string
    cleaned_text = ' '.join(tokens)

    return cleaned_text
