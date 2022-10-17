import pandas as pd
import numpy as np

df = pd.read_csv("Dataset.csv", index_col=[0],lineterminator='\n') 
df.rename( columns={'Unnamed: 0':'Index'}, inplace=True )

df["Developer"].fillna("N/A", inplace=True)

df['tags'] = df["Summary"] + df["Genres"] + df["Developer"]

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
df['tags'] = df['tags'].fillna('')
tfidf_matrix = tfidf.fit_transform(df['tags'])
tfidf_matrix.shape

from sklearn.metrics.pairwise import linear_kernel

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index, index=df['Name']).drop_duplicates()

def get_rec(name, cosine_sim=cosine_sim):
    idx = indices[name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    game_indices = [i[0] for i in sim_scores]
    return df['Name'].iloc[game_indices]
