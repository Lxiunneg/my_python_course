def bouncing_ball(h, bounce, window):
    # your code
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    count = 1
    while (h > window):
        h = h * bounce
        if h > window:
            count += 2
    return count
