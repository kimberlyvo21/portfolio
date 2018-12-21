# Kimberly Vo collab with stephen chew, julie nguyen, megan Van Rafelghem
# kv3nw.... ssc6ae, jqn5xk. mtv2mn
instructor_list = []
import urllib.request

def instructors(department):
    '''
    returns an alphabetized list of professors that teach in the department without repeating

    :param department: which department
    :return: list of teachers
    '''
    dept = department
    url = 'http://cs1110.cs.virginia.edu/files/louslist/' + str(dept)
    f = urllib.request.urlopen(url)
    for line in f:
        x = str(line)
        x = x.strip().split('|')
        professor = (x[4])
        extra = professor.find("+")
        if extra != -1:
            professor = professor[0:-2]
        if professor not in instructor_list:
            instructor_list.append(professor)
    sorted_list = sorted(instructor_list)
    return sorted_list

def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    '''
    searches for the classes that fit all the requirements given
    :param dept_name: name of department
    :param has_seats_available: seats available in the class
    :param level: level of difficulty
    :param not_before: not before a time
    :param not_after: not after a time
    :return: list of classes that meet parameters
    '''
    classes = urllib.request.urlopen(url='http://cs1110.cs.virginia.edu/files/louslist/' + dept_name).read().decode('utf-8').split('\n')
    matched_classes = []
    for line in classes:
        line = line.split('|')
        if len(line) > 1:
            if availability(has_seats_available, line) and class_before(not_before, line) and class_after(not_after, line) and class_level(level,line):
                matched_classes.append(line)
    return matched_classes

def class_level(level, line):
    '''
    searches for classes that are in the level range
    :param level: level given
    :param line: line of code being worked on
    :return:
    '''
    if level is None:
        return True
    else:
        return str(line[1])[0] == str(level)[0]


def availability(has_seats_available, line):
    '''
    searches for classes with available seats
    :param has_seats_available: how many seats available
    :param line: line being worked on
    :return:
    '''
    if has_seats_available:
        return line[15] < line[16]
    else:
        return True


def class_before(not_before, line):
    '''
    looks for classes not before a certain time
    :param not_before: time given
    :param line: line being worked on
    :return:
    '''
    start = int(line[12])
    if not_before is None:
        return True
    else:
        return start >= not_before


def class_after(not_after, line):
    '''
    searches for classes not after time given
    :param not_after: time given
    :param line: line being worked on
    :return:
    '''
    start = int(line[12])
    if not_after is None:
        return True
    else:
        return start <= not_after
