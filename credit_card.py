# Kimberly Vo
# kv3nw

def check(card):
    '''
    checkes whether a credit card number is valid
    :param card: the card number a user would like to check
    :return: returns True if the number is valid and False if it is not valid
    '''
    card= str(card)
    num = list(card)
    prev_num = 0
    prev_num3 =0
    sum_num=0
    sum3 = 0
    int_num = []
    check2_list = []
    for i in num:
        int_num.append(int(i))
    if len(int_num)%2 ==0:
        check1 = int_num[1::2]
        check2 = int_num[::2]
    else:
        check1 = int_num[::2]
        check2 = int_num[1::2]
    for j in check1:
        sum_num = prev_num +j
        prev_num = sum_num
    for k in check2:
        prev_num2 = 0
        double = k * 2
        double = str(double)
        digits = list(double)
        temp_list = []
        for i in digits:
            temp_list.append(int(i))
        for i in temp_list:
            sum2 = prev_num2 + i
            prev_num2 = sum2
        check2_list.append(sum2)
    for i in check2_list:
        sum3 = prev_num3 + i
        prev_num3 = sum3
    if (sum_num + sum3) % 10 == 0:
        return True
    else:
        return False



