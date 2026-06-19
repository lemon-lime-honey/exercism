"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return 'un'+word

def make_word_groups(vocab_words):
    number = len(vocab_words)
    for i in range(1, number):
        vocab_words[i] = vocab_words[0] + vocab_words[i]
    return ' :: '.join(vocab_words)

def remove_suffix_ness(word):
    word = word[:-4]
    if word[-1] == 'i':
        word = word[:-1] + 'y'
    return word

def adjective_to_verb(sentence, index):
    sentence = sentence[:-1]
    words = sentence.split(' ')
    return words[index] + 'en'
