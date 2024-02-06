# Write a function that accepts string from user, return a sentence with the words reversed.
# We are ready -> ready are We
def sentence(string):
    return " ".join(reversed(string.split()))
print(sentence("we are ready"))
print(sentence("I am Shugyla"))