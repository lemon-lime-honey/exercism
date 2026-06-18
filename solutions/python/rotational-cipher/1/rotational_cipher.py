def rotate(text, key):
    if key in (0, 26):
        return text
    else:
        lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
        upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_code = ''
        upper_code = ''
        result = ''
        lower_code = lower_alpha[key:] + lower_alpha[0:key]
        upper_code = upper_alpha[key:] + upper_alpha[0:key]

        for letter in text:
            if letter.isupper():
                result += upper_code[upper_alpha.find(letter)]
            elif letter.islower():
                result += lower_code[lower_alpha.find(letter)]
            else:
                result += letter
        return result

    
