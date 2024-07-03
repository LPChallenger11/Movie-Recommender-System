import numpy as np 
import pandas as pd 

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merge Two dataframes : Movies and Credits 
movies = movies.merge(credits, on='title')
# print(movies.columns)

# we select and keep required fields
movies = movies[['genres','movie_id','keywords','overview','title','cast','crew']]
# movies.info()
print(movies.head())
