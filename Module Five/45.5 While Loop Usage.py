import random
numbers = [1,2,3,4,5,6,7,8,9]

print('Games Start and Guess a number from 1-9')
print('*'*40)
computer_number = random.choice(numbers)

while True:
    number = int(input('What is your guess: '))
    if computer_number == number:
        print('congratulations')
        break
    else:
        print('Hoy Nai')
