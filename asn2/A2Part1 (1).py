from sentence_transformers import SentenceTransformer
from numpy import dot
from math import sqrt
import json

def get_tweets():
    tweets = []
    file_path= "./tweets-utf-8.json/tweets-utf-8.json"
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet_data = json.loads(line)
            if 'text' in tweet_data:
                tweets.append(tweet_data['text'])
    # print(tweets[0])
    return tweets

def cal_norm(vec):
    result = 0
    for i in range(len(vec)):
        result += vec[i]**2
    return sqrt(result)

def cosine_similarity(vec1, vec2):
    dot_product = dot(vec1, vec2)
    norm_vec1 = cal_norm(vec1)
    norm_vec2 = cal_norm(vec2)
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0  # To handle division by zero
    return dot_product / (norm_vec1 * norm_vec2)


def sort_by_sim(query_embedding,document_embeddings,documents):
    sim_docs = []
    for doc_embedding, doc in zip(document_embeddings, documents):
        similarity = cosine_similarity(query_embedding, doc_embedding)
        sim_docs.append((similarity, doc))
    sim_docs.sort(reverse=True, key=lambda x: x[0])  # Sort in decreasing order of similarity
    return sim_docs
    
def glove_top25(query,documents):
    model = SentenceTransformer('sentence-transformers/average_word_embeddings_glove.840B.300d')
    document_embeddings = model.encode(documents)
    query_embedding = model.encode(query)
    result = sort_by_sim(query_embedding,document_embeddings,documents)
    return result[:25]

def minilm_top25(query,documents):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    document_embeddings = model.encode(documents)
    query_embedding = model.encode(query)
    result = sort_by_sim(query_embedding,document_embeddings,documents)
    return result[:25]
        
# ## Test Code

tweets = get_tweets()

print("**************GLOVE*****************")
for p in glove_top25("I am looking for a job.",tweets): print(p)

print("**************MINILM*****************")
for p in minilm_top25("I am looking for a job.",tweets): print(p)
