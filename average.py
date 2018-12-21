# Kimberly Vo
# kv3nw

def mean(a,b,c):
    '''
    calculates the average of the 3 parameters
    :param a: first number
    :param b: second number
    :param c: third number
    :return: average of the 3 numbers (mean1)
    '''
    mean1 = (a+b+c)/3
    return mean1

def median(a,b,c):
    '''
    finds the number in the middle based on value
    :param a: first number
    :param b: second number
    :param c: third number
    :return: number with the middle value
    '''
    if a > b:
        if a > c:
            if c > b:
                return c
            else:
                return b
        else:
            return a
    else:
        if b > c:
            if a > c:
                return a
            else:
                return c
        else:
            return b


def rms(a,b,c):
    '''
    squares all the parameters and uses the mean function to find the average, then square root the total
    :param a: first number
    :param b: second number
    :param c: third number
    :return: root mean square
    '''
    a=a**2
    b=b**2
    c=c**2
    square = (mean(a,b,c))**(1/2)
    return square

def middle_average(a,b,c):
    '''
    finds the mean, rms, and median of the 3 numbers, then find the median of all the 3 calculated numbers.
    :param a: first number
    :param b: second number
    :param c: third number
    :return: median of the three calculations
    '''
    d = mean(a,b,c)
    e = rms(a,b,c)
    f = median(a,b,c)
    g = median(d,e,f)
    return g
