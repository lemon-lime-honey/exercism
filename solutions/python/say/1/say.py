from collections import deque

name = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 
        50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

def say(number):
    if (number < 0 ) or (number > 999999999999):
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"
    
    num = [0, 0, 0, 0]
    result = deque()
    
    if number >= 1000000000:
        num[3] = number // 1000000000
        number %= 1000000000
    if number >= 1000000:
        num[2] = number // 1000000
        number %= 1000000
    if number >= 1000:
        num[1] = number // 1000
        number %= 1000
    num[0] = number

    for index, n in enumerate(num):
        if n == 0:
            continue

        temp = list()
        
        if n >= 100:
            temp.append(name[n // 100])
            temp.append('hundred')
            n %= 100

        if n >= 10:
            if n <= 20:
                temp.append(name[n])
            else:
                if n % 10:
                    temp.append(name[n - (n % 10)] + "-" + name[n % 10])
                else:
                    temp.append(name[n])
        if (n < 10) * (n > 0):
            temp.append(name[n])
        if index == 1:
            temp.append('thousand')
        if index == 2:
            temp.append('million')
        if index == 3:
            temp.append('billion')
        result.appendleft(' '.join(temp))
    return (' '.join(result).rstrip())