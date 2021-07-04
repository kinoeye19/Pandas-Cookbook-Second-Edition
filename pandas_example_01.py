import pandas as pd
import numpy as np

movies = pd.read_csv("data/movie.csv")
columns = movies.columns
index = movies.index
data = movies.to_numpy()

# print(columns)
# print(index)
# print(data)

print(type(columns))
type(index)
type(data)
