# Kimberly Vo
# kv3nw

def binop(calculation):
    '''
    :param calculation: brings in th emath problem as a string
    :return: the calculation as an int or a float
    '''
    calculation = calculation.replace(" ","")
    if calculation.find("+") != -1:
        location = calculation.find("+")
        num1 = int(calculation[0:location])
        num2 = int(calculation[location+1:])
        newcalc = num1+num2
        return newcalc
    elif calculation.find("-") !=-1:
        location = calculation.find("-")
        num1 = int(calculation[0:location])
        num2 = int(calculation[location + 1:])
        newcalc = num1 - num2
        return newcalc
    elif calculation.find("*") != -1:
        location = calculation.find("*")
        num1 = int(calculation[0:location])
        num2 = int(calculation[location + 1:])
        newcalc = num1 * num2
        return newcalc
    elif calculation.find("/") !=-1:
        location = calculation.find("/")
        num1 = int(calculation[0:location])
        num2 = int(calculation[location + 1:])
        newcalc = num1 / num2
        return newcalc

