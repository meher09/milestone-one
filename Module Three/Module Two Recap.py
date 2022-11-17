# print('I\'m going\n\tto make tutorial')

number = 5
guess = int(input('Enter Your Number: '))

# if guess == number:
#     print('Yah, you have guessed correct number')
# elif guess > number:
#     print('You have entered larger number')
# else:
#     print('You have entered smaller number')

if guess != number:
    if guess > number:
        print('You have entered larger number')
    else:
        print('You have entered smaller number')
else:
    print('You have won the game')





