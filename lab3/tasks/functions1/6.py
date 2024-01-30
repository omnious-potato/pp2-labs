def reverseWords(source):    
    ans = ""
    whitespace = " "
    words = [x for x in source.split()]
    for x in reversed(words):
        ans += x + whitespace
    return ans




sentence = input()
print(reverseWords(sentence))