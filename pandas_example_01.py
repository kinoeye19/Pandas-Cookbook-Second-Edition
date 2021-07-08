import pandas as pd
import numpy as np

movies = pd.read_csv("data/movie.csv")
columns = movies.columns
index = movies.index
data = movies.to_numpy()

# print(columns)
# print(index)
# print(data)

# type(columns)
# type(index)
# type(data)

# print(issubclass(pd.RangeIndex, pd.Index))
# print(issubclass(columns.__class__, pd.Index))


# print(movies.dtypes)
# print(movies.dtypes.value_counts())
# print(movies.info())

# print(movies.director_name)
# print(movies.loc[:, "director_name"])
# print(movies.iloc[:, 1])
# print(movies.iloc[:, 1].index)
# print(movies.iloc[:, 1].name)
# print(movies.iloc[:, 1].dtype)
# print(movies.iloc[:, 1].size)

# print(movies.iloc[:, 1].apply(type))
# print(movies.iloc[:, 1].apply(type).unique())

director = movies["director_name"]
fb_likes = movies["actor_1_facebook_likes"]

# print(director.dtype)
# print(fb_likes.dtype)
# print(director.head())
# print(director.sample(n=5, random_state=42))
# print(fb_likes.head())

# print(director.value_counts())
# print(director.value_counts().head(4))
# print(director.shape)
# print(len(director))
# print(director.unique())

# print(fb_likes.dtype) 
# print(fb_likes.fillna(0).astype(int).head())

# print(fb_likes.isna) 
# print(fb_likes.isna()) 
# print(fb_likes.isna().sum()) 



print(
    fb_likes.fillna(0).astype(int)
    # .head(5)
)

