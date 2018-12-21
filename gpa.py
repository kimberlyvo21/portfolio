# Kimberly Vo
# kv3nw

credit = 0
current_gpa = 0

def add_course(a,b=3): #looked up online how to use global and default variable
    global credit, current_gpa
    credit_old = credit
    credit = credit+ b
    current_gpa = ((credit_old * current_gpa) + (a * b)) / credit
    return credit, current_gpa

def gpa():
    global current_gpa
    return current_gpa

def credit_total():
    global credit
    return credit
