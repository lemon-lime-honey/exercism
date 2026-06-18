def is_armstrong_number(number):
    num_to_str = str(number)
    exponent = len(num_to_str)
    result = 0
    for num in num_to_str:
        result += int(num) ** exponent
    if result == number:
        return True
    return False
