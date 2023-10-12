def naughty_or_nice(data):
    C_Naughty = 0
    C_Nice = 0

    for month in data.values():
        for day in month.values():
            if day == 'Naughty':
                C_Naughty += 1
            else:
                C_Nice += 1

    if C_Naughty > C_Nice:
        return 'Naughty!'
    else:
        return 'Nice!'
