number = int(input('Enter number: '))

if number % 2 == 0:
    if number == 0:
        print(number, 'is Zero')
    else:
        print(number, 'is even')
else:
    print(number, 'is odd')