def shorten_number(suffixes, base):
    #your code here
    def fun(num):
        if isinstance(num,str) and num.isdigit():
            num = int(num)
            for i in range(len(suffixes)):
                if i == len(suffixes)-1:
                    return f'{int(num)}{suffixes[i]}'
                elif num >= base:
                    num /= base
                else:
                    return f'{int(num)}{suffixes[i]}'
        else:
            return str(num)
    
    return fun
        