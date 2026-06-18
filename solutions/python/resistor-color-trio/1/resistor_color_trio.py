color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def label(colors):
    number = ''
    for item in colors:
        number += str(color.index(item))
    result = int(number[0:2]) * (10 ** int(number[2]))
    if result >= 1000:
        return str(result // 1000) + ' kiloohms'
    return str(result) + ' ohms'
