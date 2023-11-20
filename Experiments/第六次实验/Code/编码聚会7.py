def find_senior(lst): 
    # your code here
    max_age = 0
    ans = []
    for person in lst:
        max_age = max(max_age,person['age'])
    
    for person in lst:
        if person['age'] == max_age:
            ans.append(person)
    
    return ans