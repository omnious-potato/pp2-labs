from pprint import pprint #for beautified print in console for dict
from movie_dict import movies

def filterByCategory(movies, category=None):
    if(category == None):
        return movies
    return [x for x in movies if (x["category"]).lower() == category.lower()]


if __name__ == "__main__":
    print("Enter movie category: ", end="")
    s = input()
    print(f"Movies in category: ")
    pprint(filterByCategory(movies, s))


