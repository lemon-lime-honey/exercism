acids = {'AUG': 'Methionine', 'UUU': 'Phenylalanine','UUC': 'Phenylalanine', 
         'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine', 
         'UCA':'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 
         'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan'}

def proteins(strand):
    translated = []
    while strand != '':
        if strand[0:3] in ('UAA', 'UAG', 'UGA'):
            break
        translated.append(acids[strand[0:3]])
        strand = strand[3:]
    return translated
