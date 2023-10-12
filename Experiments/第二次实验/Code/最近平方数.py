import math


def nearest_sq(n):
    # pass
    num = int(math.sqrt(n))
    next_num = num + 1
    if (next_num ** 2 - n) < (n - num ** 2):
        return next_num ** 2
    else:
        return num ** 2
