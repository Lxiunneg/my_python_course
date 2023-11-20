def fun():
    return lambda x : x + 2

def fun_1(f = None,x:int = 0):
    return 1 if not f else f(x)
print(fun_1(fun(),x=2))