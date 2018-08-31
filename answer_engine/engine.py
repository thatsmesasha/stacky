from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
import re
import pandas as pd
import numpy as np
import scipy
import nltk
nltk.download('punkt')

print('Loading model...')
model = Doc2Vec.load('model_doc2vec/complete.model')
print('Loading dataframe...')
train_df = pd.read_json('data/train_qa_with_ids.json').sort_index()
print('Loading question vectors...')
all_q_vectors = np.load('data/train_q_numpy_vectors.npy')
print('Answer Engine ready')


def clean_html(text):
    return re.sub('<.*?>', '', text)

def get_vector(text):
    preproccessed_text = clean_html(text).lower()
    words = word_tokenize(preproccessed_text)
    vector = model.infer_vector(words, epochs=1000, min_alpha=0.025, alpha=0.025)
    return vector

def answer_default(question):
    default_response = {
        'electedAnswer': 'the answer to the question',
        'buckets': [32, 56, 12],
        'bestAnswers': [ 453, 543, 678 ]
    }
    return default_response

def answer(question):
    vector = get_vector(question)
    similarity_matrix = scipy.spatial.distance.cdist(all_q_vectors, vector.reshape(1, -1), 'cosine').reshape(-1)
    ind = np.argpartition(similarity_matrix, 3)[:3]
    ind = [ind for _,ind in sorted(zip(similarity_matrix[ind],ind))]
    electedAnswer = clean_html(train_df.loc[ind[0]].answer)
    top3a = []
    top3b = []
    for i, row in train_df.loc[ind].iterrows():
        top3a.append(row.answer_id)
        top3b.append(row.question_id)
    return {
        'electedAnswer': electedAnswer,
        'buckets': top3b,
        'bestAnswers': top3a
    }
