import re

def abbreviate(words):
    words = words.upper()
    words = re.sub(r'[_!?]', '', words)
    result = words[0]
    for num in range(1, len(words)):
        if (words[num - 1] in (' ', '-')) * (words[num].isalpha()):
            result += words[num]
    return result
        
