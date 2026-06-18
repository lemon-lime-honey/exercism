import re

truAlpha = 'abcdefghijklmnopqrstuvwxyz'
revAlpha = truAlpha[::-1]

def encode(plain_text):
    plain_text = re.sub('[ ,.!?]', '', plain_text.lower())
    result = ''
    for index, letter in enumerate(plain_text):
        if (index != 0) * (index % 5 == 0):
            result += ' '
        if letter.isalpha():
            result += revAlpha[truAlpha.index(letter)]
        else:
            result += letter
    return result

def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(' ', '')
    result = ''
    for index, letter in enumerate(ciphered_text):
        if letter.isalpha():
            result += truAlpha[revAlpha.index(letter)]
        else:
            result += letter
    return result
