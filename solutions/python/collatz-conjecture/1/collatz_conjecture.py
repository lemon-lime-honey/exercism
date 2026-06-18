def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    step = 0
    while True:
        if number == 1:
            break
        elif number % 2 == 0:
            number = number / 2
            step += 1
        else:
            number = 3 * number + 1
            step += 1
    return step
