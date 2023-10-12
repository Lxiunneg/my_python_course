def get_count(sentence):
    count = 0
    words = ['a', 'e', 'i', 'o', 'u']
    for c in sentence:
        if c in words:
            count += 1
    return count
