def uniq(L):
    unique_L = []
    for x in L:
        #naive solution
        if x not in unique_L:
            unique_L.append(x)
    return unique_L
        


test = [x for x in input().split()]
print(uniq(test))