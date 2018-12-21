# Kimberly Vo and Julie Nguyen
# kv3nw and jqn5xk
def madlib():
    place = input('What is a generic location?')
    noun = input('Put in a noun.')
    name = input('Give a name.')
    animal = input('What is your favorite animal?')
    pverb = input('Write a verb in the past tense.')
    object = input('Input a mystical object')
    TAname = input('Give the name of your favorite TA')
    replace(place, noun, name, animal, pverb, object, TAname)

def replace(place, noun, name,animal, pverb, object, TAname):
    print("Today I went to the" ,place, "and discovered a talking" ,noun+".\nIt told me to look for" ,name, "and ask for a(n)" ,animal+".\nI" ,pverb, "to find" ,name+", because honestly I had nothing to do with my day anyway.\nThis hunt led me to a" ,object, "that I used convince" ,TAname, "to give me a good grade :).")

madlib()
