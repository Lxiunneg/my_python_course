def Sum(Base:int,M:int) -> int:
    return (Base + Base * M) * M / 2

def func(number:int,n) -> int:
    temp = int(number/n)
    if number % n == 0:
        temp -= 1
    return temp

def solution(number) -> int:
    pass
    if number <= 3:
        return 0
    elif number <= 5:
        return 3
    return Sum(3, func(number,3)) + Sum(5, func(number,5)) - Sum(15, func(number,15))
    
print(solution(10))