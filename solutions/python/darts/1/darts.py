def score(x, y):
    square = x ** 2 + y ** 2
    if square <= 1:
        return 10
    elif square <= 25:
        return 5
    elif square <= 100:
        return 1
    return 0
