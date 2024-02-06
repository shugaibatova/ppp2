# Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def palin(string):
    n=len(string)
    for i in range(n-1):
        if(string[i]==string[n-1-i]):
            return True
    return False
print(palin("madam"))