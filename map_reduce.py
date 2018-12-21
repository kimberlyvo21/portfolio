# Kimberly Vo
# kv3nw

def mymap(map_func, nums):
    '''

    :param map_func: performs the function given to every element in the list
    :param nums: the list given
    :return: elements in the list that went through the function
    '''
    func_list =[]
    for i in nums:
        ans = map_func(i)
        func_list.append(ans)
    return func_list

def myreduce(reduce_func, numbers):
    '''

    :param reduce_func: performs the function multiple times throughout the list
    :param numbers: the list given
    :return: the completed function with elements in the list
    '''
    num = numbers[0]
    while len(numbers) !=0:
        if len(numbers)>1:
            ans = reduce_func(num,numbers[1])
            numbers = numbers[1:]
            num = ans
        else:
            return ans
    return ans
