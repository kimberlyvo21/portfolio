# Kimberly Vo
# kv3nw

def myfind(s,t):
    '''
    Sees if string t matches any part of string s (worked with jqn5xk)
    :param s: full word
    :param t: testing variable (to see if it's in s)
    :return: first place that t matches in s
    '''
    step = 0 #position where t matches s
    for letters in s:
        if letters == t[0]:
            counter1 = 0  # keeps track of position in t
            counter2 = step # keeps track of position in s
            for i in range(len(t)):
                if letters == t[i]:
                    counter1 +=1
                    if counter1 == len(t):
                        return step
                    letters = s[(counter2)+1]
                    counter2 += 1
        step += 1
    return -1


def mysplit(s):
    '''
    splits the input up after each space
    :param s: the phrase or word
    :return: the phrase or word split up between the spaces
    '''
    word_list = []
    space = myfind(s, " ")
    while space != -1:
        space = myfind(s, " ")
        if space != -1:
            new_word = s[0:space]
            word_list.append(new_word)
            s = s[space+1:]
        else:
            new_word = s[0:]
            word_list.append(new_word)
    return word_list
