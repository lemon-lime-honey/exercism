def append(list1, list2):
    return list1 + list2

def concat(lists):
    result = []
    for item in lists:
        if item not in result:
            result += item
    return result

def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result += [item]
    return result

def length(list):
    return len(list)

def map(function, list):
    result = []
    for item in list:
        result += [function(item)]
    return result

def foldl(function, list, initial):
    if list == []:
        return initial
    result = 0
    for index, item in enumerate(list):
        if index == 0:
            result += function(initial, item)
        else:
            result = function(result, item)
    return result

def foldr(function, list, initial):
    if list == []:
        return initial
    result = initial
    for item in list[::-1]:
        result = function(item, result)
    return result

def reverse(list):
    return list[::-1]
