def is_valid(isbn):
    if isbn == '':
        return False

    isbn = isbn.replace('-', '')

    if not len(isbn) == 10:
        return False
    if not isbn[0:9].isdigit():
        return False
    if not (isbn[9].isdigit() + (isbn[9] == 'X')):
        return False

    addi = 0

    for index in range(9):
        addi += (10 - index) * int(isbn[index])

    if isbn[9] == 'X':
        addi += 10
    else:
        addi += int(isbn[9])

    if addi % 11 == 0:
        return True
    return False
