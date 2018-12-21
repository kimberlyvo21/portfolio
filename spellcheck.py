# Kimberly Vo
# kv3nw


import urllib.request


def strip_punc(input_user):
    '''
    takes the punctuations out of the phrase
    :param input_user: the phrase the user chose
    :return: phrase without punctuations
    '''
    word_list = []
    for words in input_user:
        word_list.append(words.strip('.?!,()\"\''))
    return word_list


correct_words = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/words.txt').read().decode('utf-8').split('\n')
print('Type text; enter a blank line to end.')
user_string = input()
while user_string != '':
    clean_input = strip_punc(user_string.split())
    for part in clean_input:
        if part.lower() not in correct_words and part not in correct_words:
            print('  MISSPELLED: ' + part)
    user_string = input()
