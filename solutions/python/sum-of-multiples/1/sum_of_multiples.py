def sum_of_multiples(limit, multiples):
    multiple = list()
    addi = 0
    for number in multiples:
        multiplier = 1
        while 1:
            if number == 0:
                break
            if (multiplier * number) >= limit:
                break
            if (multiplier * number) not in multiple:
                multiple.append(multiplier * number)
                addi += multiplier * number
                multiplier += 1
            if (multiplier * number) in multiple:
                multiplier += 1
    return addi
