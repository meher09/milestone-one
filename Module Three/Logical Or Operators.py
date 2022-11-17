marks = int(input('Enter Marks: '))
weight = int(input('Enter weight: '))

if not (marks <= 79 or  weight >= 20) :
    print('You will get a chocklet')
else:
    print('You get less marks and over weight')