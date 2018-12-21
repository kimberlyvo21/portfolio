# Kimberly Vo
# kv3nw

word = input('Enter a word to guess: ')
word = word.lower()
if word == word:
    blanks = "_".join(word) + "_"

    print("The word to guess", blanks[1::2])
    guess = input('Guess a letter: ')
    if word.find(guess)!=-1:
        blanks = blanks.replace(guess+"_",guess+guess)
        print("The word to guess",blanks[1::2])
        guess= input('Guess a letter: ')
    else:
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    if word.find(guess) != -1:
        blanks = blanks.replace(guess + "_", guess + guess)
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    else:
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    if word.find(guess) != -1:
        blanks = blanks.replace(guess + "_", guess + guess)
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    else:
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    if word.find(guess) != -1:
        blanks = blanks.replace(guess + "_", guess + guess)
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    else:
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    if word.find(guess) != -1:
        blanks = blanks.replace(guess + "_", guess + guess)
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    else:
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    if word.find(guess) != -1:
        blanks = blanks.replace(guess + "_", guess + guess)
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    else:
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    if word.find(guess) != -1:
        blanks = blanks.replace(guess + "_", guess + guess)
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    else:
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    if word.find(guess) != -1:
        blanks = blanks.replace(guess + "_", guess + guess)
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    else:
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    if word.find(guess) != -1:
        blanks = blanks.replace(guess + "_", guess + guess)
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    else:
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    if word.find(guess) != -1:
        blanks = blanks.replace(guess + "_", guess + guess)
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
    else:
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')

