import re

class Luhn:
    def __init__(self, card_num):
        self.num = re.sub(' ', '', card_num)

    def valid(self):
        num = self.num
        if len(num) <= 1 or not all(i.isnumeric() for i in num):
            return False
        
        result = [int(i) for i in num]
        result[-2::-2] = [2 * i - 9 * (i > 4) for i in result[-2::-2]]
        return not (sum(result) % 10)