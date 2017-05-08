import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

doc_zip = 'movies.zip'
movies_csv = 'movies.csv'
ratings_csv = 'ratings.csv'
rutazip = 'ml-latest-small'

movie_names = ['movie_id', 'title', 'genres']
rating_names = ['user_id', 'movie_id', 'rating', 'timestamp']

# Reading the files needed for this analysis
movies = pd.read_csv(
    rutazip +'/'+ movies_csv,
    sep=',',
    names=movie_names)
ratings = pd.read_csv(
    rutazip +'/'+ ratings_csv,
    sep=',',
    names=rating_names)


rated_movies = pd.merge(movies, ratings, on='movie_id')
rated_movies = rated_movies.sort_values('rating', ascending=False)
# ['movie_id', 'title', 'genres', 'user_id', 'rating', 'timestamp']

rated_movies['rating'] = pd.to_numeric(rated_movies['rating'][1:100005])
grouped = rated_movies.groupby('title').mean()
kgrouped = grouped.to_dict()['rating']
#print(grouped)

dic={}
for s in kgrouped.values():
	s = round(s)
	if(s.is_integer()):
		dic[int(s)] = dic.get(s, 0) + 1

val=list(dic.values())
mx=max(val)
val_mx = []
for i in val:
	val_mx.append(i/mx)
key=list(dic.keys())

#print(val)
#print(val_mx)
#print(key)
plt.bar(key,val)
plt.title('Distribucion de rating')
plt.xlabel('Ratings');
plt.ylabel('Cantidad de peliculas');
#plt.hist([1, 2, 1])
plt.show()

top5 = grouped.sort_values('rating', ascending=False)[0:5]
print(top5)
