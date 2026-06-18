from itertools import zip_longest

def transpose(lines):
    sentences = zip_longest(*lines.split('\n'), fillvalue='@')
    result = '\n'.join(''.join(sentence).rstrip('@').replace('@', ' ') for sentence in sentences)
    return result