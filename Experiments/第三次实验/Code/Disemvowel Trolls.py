def disemvowel(string_):
    vowels = ['a','A','o','O','e','E','i','I','u','U']
    
    for c in vowels:
        string_ = string_.replace(c,'')
    
    return string_