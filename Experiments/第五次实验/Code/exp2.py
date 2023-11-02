def find_outlier(integers):
    temp = [i%2 for i in integers]
    return integers[temp.index(1)] if sum(temp) == 1 else integers[temp.index(0)]