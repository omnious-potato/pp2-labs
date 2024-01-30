def isPalindrome(src):
    n = int(len(src))
    for x in range(0, int(n/2)):
        if(src[x] != src[n - x - 1]):
            return False
    return True

# s = input()
# print(isPalindrome(s))