from string import ascii_lowercase

def is_pangram(sentence):
    # remove letters in the sentence except alphabet
    purified = str(filter(str.isalpha, sentence)).lower()
    # get length of the filtered sentence
    length = len(purified)

    # if the sentence doesn't have any alphabet,
    # return 'False'
    if (length == 0):
        return False

    # make a list which is consist of alphabets
    abc = list(ascii_lowercase)

    # remove the letters
    for i in range(length):
        if (purified[i] in abc):
            abc.remove(purified[i])

    # if the list is empty, return 'True'
    # if not, return 'False'
    if (not abc):
        return True
    
    return False
    pass
