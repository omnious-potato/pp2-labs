def filterPrimes(input_list):
    return list(filter(lambda x: (not any(x % i == 0 for i in range(2, int(x**(1/2) + 1)))) and not x == 1, input_list))

if __name__ == "__main__":
    N = int(input("Enter up to which number primes gonna be generated "))
    L = list(range(1, N + 1))

    L_primes = filterPrimes(L)

    #print(L_primes)
    print(f"Amount of primes from 1 to {N}: {len(L_primes)}")

    