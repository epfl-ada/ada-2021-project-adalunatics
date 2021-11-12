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

def process_chunk(chunk, proc_function, keywords, save_path):
    '''This function process a chunk of a dataset using the processing function given and save the preprocessed results to the path       given'''
    print(f'Processing chunk with {len(chunk)} rows')
    # Remove Phase and Num of occurences columns (not useful and redundant, respectively) to save memory
    chunk.drop(['phase', 'numOccurrences'], axis=1)
    # Apply the processing function
    chunk = proc_function(chunk, keywords)
    if len(chunk) > 0:
        print(f'There are {len(chunk)} rows that include some of the keywords')
        chunk['quotation'].to_csv(path_or_buf=save_path, compression='bz2', mode='a')
    return chunk

def manual_extraction(df, keywords):
    '''This function extracts rows in which their quotes contain any of the keywords given.'''
    results = df['quotation'].str.contains('|'.join(keywords))
    indices = list(results[results == True].index)
    return df.loc[indices,:]

def parse_title(hostname, url, positions):  
  try:
    res = get_tld(url[2:-2], as_object=True)
 
    if hostname in positions:
        return res.parsed_url.path.split('/')[positions[hostname]]
    else:
        return 0
  except:
    pass
    
def get_hostname(urls): 
   result = []

   list_urls = urls[1:-1].replace("'", "").replace(" ", "").split(",")
   for url in list_urls:
    parsed_url = urllib.parse.urlparse(url)
    print(parsed_url)
    result.append('{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url))
    #print('{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url))
   return result

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

def ids_to_tweets(tweet_ids, api):
    '''This function fetches tweets based on their IDs'''
    counter = 0
    ids = []

    with open(tweet_ids, 'r') as txtfile:
        lineReader = txtfile.readlines()
        for row in lineReader:
            ids.append(row)
            
    print(len(ids))
    sleepTime = 2
    tweets_data = {'tweet': [],
                  'date': [],
                  'location': []}

    for id in ids[10000:20000]:
        try:
            tweetFetched = api.get_status(id)
            tweets_data['tweet'] = tweetFetched.text
            tweets_data['date'] = tweetFetched.created_at
            tweets_data['location'] = tweetFetched.user.location
            df = pd.DataFrame(tweets_data, index=[id])
            # print('in')
            df.to_csv(path_or_buf='/content/drive/Shareddrives/ADA LUNATICS 2021/datasets/tweets_data.csv.bz2',                   compression='bz2', mode='a')
            # tweets_data['fav_count'].append(tweetFetched.retweeted_status.user.favourites_count)
            time.sleep(sleepTime)

        except Exception as e:
            print(e)
            counter += 1
            time.sleep(sleepTime)
            continue
    print(counter)
    # tweets_data = pd.DataFrame.from_dict(tweets_data)
    return tweets_data

def embedSentence(sentence, word_vectors):
    '''This function maps the words in a scentence to their embeddings'''
    embed = map(lambda x: embedding(x, word_vectors), sentence)
    return list(embed)

def embedding(word, word_vectors):
    '''This function extracts word embeddings'''
    try:
        embed = word_vectors[word]
    except Exception:
        embed = word_vectors['unk']
    return embed

def averageEmbedding(sentence):
    '''This function averages words embedding in a scentence to get one embedding for each scentence'''
    average = np.mean(sentence, axis=0)
    return average

def featurize(sentence, dataframe, FeatureColumns):
    '''This function creates a dataframe containing the embeddings in each column'''
    sentence = pd.Series(sentence, index=FeatureColumns)
    dataframe = dataframe.append(sentence, ignore_index=True)
    return dataframe


def plotWords(dataframe, fileCount=0):
    '''This function plots the quotes (tSNE values) on a 2D Plane'''
    plt.figure(num=None, figsize=(12,8), dpi=300)
    ax = plt.subplot(111)
    for i in range(dataframe.shape[0]):
        plt.text(dataframe.iloc[i,0], dataframe.iloc[i,1], str(dataframe.iloc[i,2]),
                color='blue',
                fontdict={'weight': 'light', 'size':2})
    
    plt.axis('off')
    plt.savefig(fname='plot'+str(fileCount), dpi=300)
    