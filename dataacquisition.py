#For Acquiring data

import numpy as np
import pandas as pd
import requests, zipfile, io    # We import all the necessary libraries.


# Get the url for ml-100k
zip_file_url = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"


# Get the files and extract them
print("Downloading movielens data...")
r = requests.get(zip_file_url, stream=True)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
print("Done.")


users_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=users_cols, encoding='latin-1')

users.shape
users.head()
genre_cols = [
    "genre_unknown", "Action", "Adventure", "Animation", "Children", "Comedy",
    "Crime", "Documentary", "Drama", "Fantasy", "FilmNoir", "Horror",
    "Musical", "Mystery", "Romance", "SciFi", "Thriller", "War", "Western"
]
items_cols = ['movie_id', 'title', 'release_date', "video_release_date", "imdb_url"] + genre_cols
items_raw = pd.read_csv('ml-100k/u.item', sep='|', names=items_cols, encoding='latin-1')

ratings_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=ratings_cols, encoding='latin-1')

from utils import create_directory #Saving the data


# Save the data
users.to_csv("data/users.csv", index=None)
items_raw.to_csv("data/items_raw.csv", index=None)
ratings.to_csv("data/ratings.csv", index=False)

