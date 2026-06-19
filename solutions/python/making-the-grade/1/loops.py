"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    scores = []
    for index in range(len(student_scores)):
        scores.append(round(student_scores[index]))
    return scores

def count_failed_students(student_scores):
    count = 0
    for index in range(len(student_scores)):
        if student_scores[index] <= 40:
            count += 1
    return count

def above_threshold(student_scores, threshold):
    above = []
    for index in range(len(student_scores)):
        if student_scores[index] >= threshold:
            above.append(student_scores[index])
    return above

def letter_grades(highest):
    grades = [41]
    delta = round((highest - 40) / 4)
    for number in range(3):
        grades.append(grades[-1] + delta)
    return grades

def student_ranking(student_scores, student_names):
    rank = []
    for index in range(len(student_scores)):
        temp = str(index + 1) + '. ' + student_names[index] + ": " + str(student_scores[index])
        rank.append(temp)
    return rank

def perfect_score(student_info):
    for index in range(len(student_info)):
        if student_info[index][1] == 100:
            return student_info[index]
    return []
