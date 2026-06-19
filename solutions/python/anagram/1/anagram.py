def find_anagrams(word, candidates):
    result = list()
    low_word = word.lower()
    letters = list(low_word)
    letters.sort()
    for item in candidates:
        low_item = item.lower()
        if low_item == low_word:
            continue
        else:
            temp = list(low_item)
            temp.sort()
            if temp == letters:
                result.append(item)
    return result
