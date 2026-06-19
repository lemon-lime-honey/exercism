def decode(string):
    result = list()
    cnt = list()
    for letter in string:
        if letter.isdigit():
            cnt.append(letter)
        else:
            if not cnt:
                result.append(letter)
            else:
                result.append(letter * int(''.join(cnt)))
                cnt = list()
    return (''.join(result))

def encode(string):
    if string == '':
        return ''
    result = list()
    before = string[0]
    cnt = 0
    for letter in string:
        if letter == before:
            cnt += 1
        else:
            if cnt == 1:
                result.append(before)
                before = letter
            else:
                result.append(str(cnt))
                result.append(before)
                before = letter
                cnt = 1
    if cnt == 1:
        result.append(before)
    else:
        result.append(str(cnt))
        result.append(before)
    return (''.join(result))