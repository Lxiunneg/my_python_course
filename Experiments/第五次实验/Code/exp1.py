def spin_words(sentence):
    # Your code goes here
    vocas = sentence.split(' ')
    res = ''
    for i in range(0,len(vocas)):
        voca = vocas[i]
        if len(voca) >= 5:
            vocas[i] = voca[::-1]
    for voca in vocas:
        res = res + voca + ' '
    return res.rstrip()

print(spin_words('Hey fellow warriors'))