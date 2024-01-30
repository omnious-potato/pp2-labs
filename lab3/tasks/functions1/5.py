def permute(src, sz = 0):
    if sz == len(src):
        print("".join(src))
    

    for i in range(sz, len(src)):
        temp = [ch for ch in src]
        temp[sz], temp[i]= temp[i], temp[sz] #swap

        permute(temp, sz + 1)
        
s = input()
permute(s)
