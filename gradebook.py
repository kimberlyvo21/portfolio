# Kimberly Vo
# kv3nw

score = {

}

credit = {

}


def total(proportions):
    '''
    calculates the weighted grade average with the scores in the dict
    :param proportions: the grade ratios
    :return: weighted grade
    '''
    global score
    global credit
    global grade_total
    grade_total = 0
    for key in proportions.keys():
        if key in score.keys():
            grade_total += proportions.get(key) * (score.get(key)/credit.get(key))
        else:
            grade_total += proportions.get(key) * 0

    return grade_total


def assignment(kind, grade, weight=1):
    '''
    puts scores and credits in the right dictionary
    :param kind: type of assignment
    :param grade: score out of 100 the person received
    :param weight: how much the assignment is weighted
    :return: nothing
    '''
    global score
    global credit
    if kind in score:
        cred_calc = credit[kind] + weight
        credit[kind] = cred_calc
        new_score = score[kind] +(grade*weight)
        score[kind] = new_score
    else:
        credit[kind] = weight
        score[kind] = (grade*weight)
