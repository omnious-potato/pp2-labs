
from task_3 import filterByCategory
from task_4 import averageScore
from movie_dict import movies
import pprint


if __name__ == "__main__":
    print("Enter movie category to calculate avergae score of: ", end="")
    category = input()
    list = filterByCategory(movies, category)
    score = averageScore(list)
    print(f"Average score is {score:.2f}")
    pprint.pprint(list)