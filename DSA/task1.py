# The longest sentence in the given text

# split S into sentences based on '.','?' and '!'
# For each sentence split sentences into words based on spaces
# Count the number of valid words i.e. words with atleast one letter
# Keep track of the max number of valid words found in any sentence
# Return the max no. of words

def solution(S):
    import re

    sentences = re.split(r'[.?!]', S)

    max_words = 0

    for sentence in sentences:
        words = sentence.split()

        valid_words = [word for word in words if re.search(r'[a-zA-Z]', word)]
        max_words = max(max_words, len(valid_words))

    return max_words

S = "We test coders. Give us a try?"

print(solution(S))