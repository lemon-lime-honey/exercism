def square(number):
    if (number > 0) * (number < 65):
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")

def total():
    total = 0
    for number in range(64):
        total += 2 ** number
    return total
