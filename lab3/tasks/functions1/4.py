def isPrime(x):
    if(x == 0 or x == 1):
        return False
    elif(x == 2 or x == 3):
        return True
    
    naive_upper_bound = int(x ** (1/2))
    for i in range(2, naive_upper_bound + 1):
        if(x % i == 0):
            return False
    return True

def filter_prime(L):
    L[:] = [x for x in L if isPrime(x)]



# l = [int(x) for x in input().split()]
# filter_prime(l)
# print(l)