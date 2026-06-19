def is_paired(input_string):
    bracket = {'(': ')', '{': '}', '[': ']'}
    close = [')', '}', ']']

    temp = ''

    for item in input_string:
        if item in bracket:
            temp += item
        elif item in close:
            if temp == '':
                return False
            else:
                if item == bracket[temp[-1]]:
                    temp = temp[:-1]
                else:
                    return False
    if temp == '':
        return True
    return False
            
