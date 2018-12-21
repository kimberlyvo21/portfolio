# Kimberly Vo
# kv3nw

word = input('Enter a word to guess: ')
word = word.lower()
blanks = "_".join(word) + "_"
print("The word to guess", blanks[1::2])
guess = input('Guess a letter: ')
n=0
while blanks[1::2] != word:
    if word.find(guess)!=-1:
        print(guess,"is a letter in the word!")
        blanks = blanks.replace(guess+"_",guess+guess)
        print("The word to guess",blanks[1::2])
        guess= input('Guess a letter: ')
        if blanks[1::2] == word:
            print("YAY!! You guessed the word!")
    else:
        n+=1
        print("sorry",guess, "is not a letter in the word")
        print("That was mistake number:",n)
        print("The word to guess", blanks[1::2])
        guess = input('Guess a letter: ')
