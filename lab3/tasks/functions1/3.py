def solve(numheads, numlegs):
    #4 legs on a (typical) rabbit, 2 legs on a (typical) chicken

    rabbits = int(numlegs/2 - numheads)
    chickens = int(numheads - rabbits)

    return (chickens, rabbits)

ans = solve(35, 94)
print(f"There are {ans[0]} chickens and {ans[1]} rabbits in a farm!")