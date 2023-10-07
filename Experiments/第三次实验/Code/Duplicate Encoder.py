def duplicate_encode(word):
    dict = {}
    for c in word:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
        
    print(dict['a'])
    
