import json
from collections import ChainMap
from itertools import count
from imdb import IMDb

movie_names_directors = {'movies': []}

# create an instance of the IMDb class
ia = IMDb()

# get a movie
bottom_movies_100 = ia.get_bottom100_movies()

movie_count = len(bottom_movies_100)
for i in range(movie_count):
    x = ia.get_movie(ia.get_imdbID(bottom_movies_100[i]))
    print("Index I= "+ str(i))
    print(x)
    direction = []
    for director in x['directors']:
        print("Director Name/Names: " + director['name'])
        direction.append(director['name'])

    movie_names_directors['movies'].append({
            str(bottom_movies_100[i]): direction
        })
print(movie_names_directors)

y = json.loads(json.dumps(movie_names_directors))
print(type(y))
z = y['movies']
z = dict(ChainMap(*z))

movie_names_directors_sorted = {k: v for k, v in sorted(z.items())}
print(movie_names_directors_sorted)

with open('movie_names_directors_sorted.json', 'w') as outfile:
    json.dump(movie_names_directors_sorted, outfile, indent=4, sort_keys=True)
