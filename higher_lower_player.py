# Kimberly Vo
# kv3nw

print("Think of a number between 1 and 100 and I'll guess it.")
guesses = int(input('How many guesses do I get? '))
num_high = 100
num_low = 0
num = int((num_low+num_high)//2)
answer = input('Is the number higher, lower, or the same as '+ str(num)+'? ')
while guesses > 0:
    if answer == "lower":
        num_high = num
        num = int((num_low+num_high)//2)
        guesses = guesses - 1
        if num_low == num_high-1 or num_high == num_low+1:
            print('Wait; how can it be both higher than '+ str(num_low)+ ' and lower than '+ str(num_high)+'?')
            break
    elif answer == "higher":
        num_low = num
        num = int((num_low+num_high)//2)
        guesses = guesses-1
        if num_low == num_high-1 or num_high == num_low+1:
            print('Wait; how can it be both higher than '+ str(num_low)+ ' and lower than '+ str(num_high)+'?')
            break
    elif answer == "same":
        print('I won!')
        break
    if guesses != 0:
        answer = input('Is the number higher, lower, or the same as ' + str(num) + '? ')
if guesses == 0:
    real_num = int(input('I lost; what was the answer? '))
    if int(num_low) > int(real_num):
        print("That can't be; you said it was higher than "+str(num_low)+"!")
    elif num_high < real_num:
        print ("That can't be; you said it was lower than "+ str(num_high)+ "!")
    else:
        print('Well played!')

