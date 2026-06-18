def flat(iterable, result):
    for item in iterable:
        if type(item) == list:
            flat(item, result)
        elif type(item) == int:
            result.append(item)
        elif item is None:
            continue

def flatten(iterable):
    result = []
    flat(iterable, result)
    return result
