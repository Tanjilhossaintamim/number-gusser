# gussing game using python
import random
low = 1
high = 50

correct_ans = random.randint(low, high)

count = 0
while count < 6:

    count += 1

    user_ans = int(input('Guss A Number Between 1 to 50 : '))
    if correct_ans > user_ans:
        print(' Correct answer is greater!')
    elif correct_ans < user_ans:
        print('Correct answer is smaller!')
    else:
        print('You Win !')
        break
    if count == 5:
        print('You Lose !')
        break
