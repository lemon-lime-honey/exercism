"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    scores = []
    for score in enumerate(student_scores):
        scores.append(round(score[1]))
    return scores

def count_failed_students(student_scores):
    count = 0
    for score in enumerate(student_scores):
        if score[1] <= 40:
            count += 1
    return count

def above_threshold(student_scores, threshold):
    above = []
    for score in enumerate(student_scores):
        if score[1] >= threshold:
            above.append(score[1])
    return above

def letter_grades(highest):
    grades = [41]
    delta = round((highest - 40) / 4)
    number = 0
    while number != 3:
        grades.append(grades[-1] + delta)
        number += 1
    return grades

def student_ranking(student_scores, student_names):
    rank = []
    for index, score in enumerate(student_scores):
        temp = str(index + 1) + '. ' + student_names[index] + ': ' + str(score)
        rank.append(temp)
    return rank

def perfect_score(student_info):
    for info in enumerate(student_info):
        if info[1][1] == 100:
            return info[1]
    return []
