import numpy as np
import pandas as pd
import re
import nltk
# We need this dataset in order to use the tokenizer
nltk.download('punkt')
from nltk.tokenize import word_tokenize
# Also download the list of stopwords to filter out
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def process_chunk(chunk, proc_function, save_path):
    '''This function process a chunk of a dataset using the processing function given and save the preprocessed results to the path       given'''
    print(f'Processing chunk with {len(chunk)} rows')
    # Remove Phase and Num of occurences columns (not useful and redundant, respectively) to save memory
    chunk.drop(['phase', 'numOccurrences'], axis=1)
    # Apply the processing function
    chunk = proc_function(chunk, _KEYWORDS)
    if len(chunk) > 0:
        print(f'There are {len(chunk)} rows that include some of the keywords')
        chunk['quotation'].to_csv(path_or_buf=save_path, compression='bz2', mode='a')
    return chunk

def manual_extraction(df, keywords):
    '''This function extracts rows in which their quotes contain any of the keywords given.'''
    results = df['quotation'].str.contains('|'.join(keywords))
    indices = list(results[results == True].index)
    return df.loc[indices,:]

def parse_title(url):
    '''This function parses the title from url'''
    res = get_tld(url, as_object=True)
    return res.parsed_url.path.split('/')[1]

def process_text(text):
    '''This function process the quotes by removing stopping words, lower casing all text and stemming them to their roots.'''
    # Make all the strings lowercase and remove non alphabetic characters
    text = re.sub('[^A-Za-z]', ' ', text.lower())

    # Tokenize the text; this is, separate every sentence into a list of words
    # Since the text is already split into sentences you don't have to call sent_tokenize
    tokenized_text = word_tokenize(text)

    # Remove the stopwords and stem each word to its root
    clean_text = [
        stemmer.stem(word) for word in tokenized_text
        if word not in stopwords.words('english')
    ]
    # Remember, this final output is a list of words
    return clean_text