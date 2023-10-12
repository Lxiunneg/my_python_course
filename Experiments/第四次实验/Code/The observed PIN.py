observed = '14'

def get_pins(observed):
    pass # TODO: This is your job, detective! 

    PINs = []
    
    numbers = {
        '1':['1','2','4'],
        '2':['2','1','3','5'],
        '3':['3','2','6'],
        '4':['4','1','5','7'],
        '5':['5','2','4','6','8'],
        '6':['6','3','5','9'],
        '7':['7','4','8'],
        '8':['8','5','7','9','0'],
        '9':['9','6','8'],
        '0':['0','8']
    }
    
    temp = ''
    
    
    def dfs(deepth):
        nonlocal temp
        if deepth == len(observed):
            PINs.append(temp)
            return
        
        for number in numbers[observed[deepth]]:
            temp = temp + number 
            dfs(deepth + 1)
            temp = temp[:-1]
        
        return
    
    dfs(0)
    
    return PINs

print(get_pins(observed))