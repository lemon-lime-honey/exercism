alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rows(letter):
    the_index = alphabet.index(letter)
    result = []

    for count in range(the_index):
        margin = the_index - count
        middle = 2 * count - 1
        if count == 0:
            result.append(' ' * margin + alphabet[count] + ' ' * margin)
        else:
            result.append(' ' * margin + alphabet[count] + ' ' * middle + alphabet[count] + ' ' * margin)

    for count in range(the_index, -1, -1):
        margin = the_index - count
        middle = 2 * count - 1
        if count == 0:
            result.append(' ' * margin + alphabet[count] + ' ' * margin)
        else:
            result.append(' ' * margin + alphabet[count] + ' ' * middle + alphabet[count] + ' ' * margin)

    return result