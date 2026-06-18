subjects = {1: 'the house that Jack built',
            2: 'the malt', 
            3: 'the rat',
            4: 'the cat', 
            5: 'the dog', 
            6: 'the cow with the crumpled horn', 
            7: 'the maiden all forlorn', 
            8: 'the man all tattered and torn', 
            9: 'the priest all shaven and shorn', 
            10: 'the rooster that crowed in the morn', 
            11: 'the farmer sowing his corn', 
            12: 'the horse and the hound and the horn'}
word = {2: 'that lay in',
        3: 'that ate',
        4: 'that killed',
        5: 'that worried',
        6: 'that tossed',
        7: 'that milked',
        8: 'that kissed',
        9: 'that married',
        10: 'that woke',
        11: 'that kept',
        12: 'that belonged to'}

def recite(start_verse, end_verse):
    sentence = []
    for number in range(start_verse, end_verse + 1):
        temp = ['This is']
        for index in range(number, 1, -1):
            temp.append(subjects[index])
            temp.append(word[index])
        temp.append(subjects[1])
        sentence.append(' '.join(temp) + '.')
    return sentence
