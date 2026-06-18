def score(word):
    result = 0;
    word = word.upper()
    for letter in word:
        if letter in 'AEIOULNRST':
            result += 1
        elif letter in 'DG':
            result += 2
        elif letter in 'BCMP':
            result += 3
        elif letter in 'FHVWY':
            result += 4
        elif letter == 'K':
            result += 5
        elif letter in 'JX':
            result += 8
        elif letter in 'QZ':
            result += 10
    return result