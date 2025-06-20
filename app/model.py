import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_recommendations(user_id, ratings, movies):
    user_movie_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
    similarity = cosine_similarity(user_movie_matrix)
    sim_df = pd.DataFrame(similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)
    
    similar_users = sim_df[user_id].sort_values(ascending=False)[1:6]
    user_movies = user_movie_matrix.loc[user_id]
    recommendations = pd.Series(dtype='float64')
    
    for sim_user_id, sim_score in similar_users.items():
        sim_user_ratings = user_movie_matrix.loc[sim_user_id]
        weighted_ratings = sim_user_ratings * sim_score
        recommendations = recommendations.add(weighted_ratings, fill_value=0)
    
    recommendations = recommendations.drop(user_movies[user_movies > 0].index, errors='ignore')
    top_movies = recommendations.sort_values(ascending=False).head(5).index.astype(int)
    return movies[movies['movieId'].isin(top_movies)]['title'].tolist()