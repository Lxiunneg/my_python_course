def fillable(stock, merch, n):
    # Your code goes here.
    if merch not in stock:
        return False
    return stock[merch] >= n