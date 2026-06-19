"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

def get_rounds(number):
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    if number in rounds:
        return True
    return False

def card_average(hand):
    add = sum(hand)
    return add / len(hand)

def approx_average_is_average(hand):
    first_last_avg = (hand[0] + hand[-1]) / 2
    median = hand[int((len(hand) - 1) / 2)]
    true_avg = card_average(hand)
    if (first_last_avg == true_avg) or (median == true_avg):
        return True
    return False

def average_even_is_average_odd(hand):
    even = hand[::2]
    odd = hand[1::2]
    if card_average(even) == card_average(odd):
        return True
    return False

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    return hand
