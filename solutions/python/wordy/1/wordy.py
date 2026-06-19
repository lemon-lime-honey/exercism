def answer(question):
    question = question.replace('What is ', '').replace('?', '').replace('plus', '+').replace('minus', '-').replace('multiplied by', '*').replace('divided by', '/').split(' ')
    question.insert(0, '(')
    question.insert(4, ')')

    for item in question:
        if (item.isalpha()) * (item not in ('What', 'is')):
            raise ValueError('unknown operation')

    try:
        return eval(' '.join(question))
    except:
        raise ValueError('syntax error')