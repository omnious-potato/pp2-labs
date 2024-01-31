from movie_dict import movies

def averageScore(list):
    sum = 0
    for x in list:
        sum += float(x["imdb"])
    return float(sum / len(list))

if __name__ == "__main__":
    print(f"Calculated IMDB average of the movie list is {averageScore(movies):.4f}")