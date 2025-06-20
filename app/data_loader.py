import pandas as pd

def load_data():
    movies = pd.read_csv("app/data/movies.csv")
    ratings = pd.read_csv("app/data/ratings.csv")
    return movies, ratings