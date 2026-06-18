SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'

def sublist(list_one, list_two):
    temp_one = ','.join(map(str, list_one)) + ','
    temp_two = ','.join(map(str, list_two)) + ','

    if temp_one == temp_two:
        return EQUAL
    if temp_one == ',' or temp_two.find(temp_one) != -1:
        return SUBLIST
    if temp_two == ',' or temp_one.find(temp_two) != -1:
        return SUPERLIST
    return UNEQUAL