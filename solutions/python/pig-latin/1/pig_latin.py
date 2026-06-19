vowel = ['a', 'e', 'i', 'o', 'u']
vowel_like = ['xr', 'yt']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 
             'k', 'l', 'm', 'n', 'p', 'q', 'r', 
             's', 't', 'v', 'w', 'x', 'y', 'z']

def convert(text):
    if (text[0] in vowel) + (text[0:2] in vowel_like):
        text += 'ay'
        return text
    buffer = ''
    while 1:
        if text[0:2] == 'qu':
            buffer += text[0:2]
            text = text[2:]
            text = text + buffer + 'ay'
            break
        if (text[0] == 'y') * (buffer != '') + (text[0] in vowel):
            text = text + buffer + 'ay'
            break
        buffer += text[0]
        text = text[1:]
    return text

def translate(text):
    result = ''
    words = text.split(' ')
    for item in words:
        result += convert(item) + ' '
    result = result.rstrip()
    return result
