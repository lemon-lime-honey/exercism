"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    value = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    return value[card]

def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    return card_two

def value_of_ace(card_one, card_two):
    if (card_one == 'A') or (card_two == 'A'):
        return 1
    if (value_of_card(card_one) + value_of_card(card_two)) < 11:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    if card_one == 'A':
        if value_of_card(card_two) == 10:
            return True
        return False
    elif card_two == 'A':
        if value_of_card(card_one) == 10:
            return True
        return False
    return False

def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False

def can_double_down(card_one, card_two):
    add = value_of_card(card_one) + value_of_card(card_two)
    if add in [9, 10, 11]:
        return True
    return False
