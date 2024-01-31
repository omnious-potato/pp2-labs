from pprint import pprint #for beautified print in console for dict
from movie_dict import movies
from task_1 import isScoredOkay


def moviesHigherThan(L=movies):
    return [x for x in L if isScoredOkay(x)]


if __name__ == "__main__":
    print("Task 2 - filter list (score > 5.5)")
    pprint(moviesHigherThan())