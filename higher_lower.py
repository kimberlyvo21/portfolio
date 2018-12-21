# Kimberly Vo
# kv3nw
import random
random_num = random.randrange(1,100)

num = int(input("What should the answer be? "))
guesses = int(input("How many guesses? "))
n_guess = 0
if num == -1:
    num = random_num
    student_guess = 0
    for i in range(guesses):
        n_guess += 1
        student_guess = int(input('Guess a number: '))
        if n_guess == guesses:
            if student_guess == num:
                print('You win!')
            else:
                print('You lose; the number was'+str(num)+".")
        elif student_guess > num:
            print("The number is lower than that.")
        elif student_guess < num:
            print("The number is higher than that.")
        elif student_guess == num:
            print("You win!")
            break
else:
    student_guess = 0
    for i in range(guesses):
        n_guess +=1
        student_guess=int(input('Guess a number: '))
        if n_guess == guesses:
            if student_guess == num:
                print ('You win!')
            else:
                print ('You lose; the number was' + str(num)+".")
        elif student_guess > num:
            print("The number is lower than that.")
        elif student_guess < num:
            print("The number is higher than that.")
        elif student_guess == num:
            print ("You win!")
            break
