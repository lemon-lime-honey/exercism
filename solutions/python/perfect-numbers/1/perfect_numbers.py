def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return 'deficient'

    aliquot_sum = 0
    for index in range(1, number):
        if (number % index == 0):
            aliquot_sum += index
    if aliquot_sum == number:
        return 'perfect'
    elif aliquot_sum > number:
        return 'abundant'
    return 'deficient'
