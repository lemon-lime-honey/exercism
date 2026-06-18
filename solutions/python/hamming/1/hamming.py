def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    length = len(strand_a)
    count = 0
    for index in range(length):
        if strand_a[index] != strand_b[index]:
           count += 1
    return count