def square_root(number):
    for i in range(1, number // 2 + 1):
        if i * i == number: return i

    return 1