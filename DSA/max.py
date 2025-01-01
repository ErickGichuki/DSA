def solution(S):
    import re
    sentences = re.split(r'[.?!]', S)
    max_words = 0

    for sentence in sentences:
        words = sentence.split()
        valid_words = [word for word in words if re.search(r'[a-zA-Z]', word)]
        max_words = max(max_words, len(valid_words))
    return max_words

S='We test coders. Give us a try?'
print(solution(S))