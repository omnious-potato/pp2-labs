#Task 1 - return true is score above 5.5
def isScoredOkay(movie, okayScore=5.5): 
    if(movie["imdb"] > okayScore):
        return True
    return False