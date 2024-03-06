#movie dict 
#category - films count
from movie_dict import movies
import pprint

if __name__ == "__main__":
    categories = {}
    for movie in movies:
        categories[str(movie["category"])] = 0
    for movie in movies:
        categories[str(movie["category"])] += 1
    

    print(categories)


    