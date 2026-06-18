def primes(limit):
    num = []
    for i in range(2, limit + 1):
        for j in range(2, limit + 1):
            if i % j == 0:
                if i == j:
                    num.append(i)
                    break
                break
    return num
