def count_developers(lst):
    # Your code here
    count = 0
    for l in lst:
        if l['continent'] == 'Europe' and l['language'] == 'JavaScript':
            count += 1
    return count