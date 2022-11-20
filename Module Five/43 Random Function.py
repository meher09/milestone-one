import random
ludu = [1,2,3,4,5,6]
random_number = random.choice(ludu)
if random_number == 6:
    print('yah, You have won the game')
else:
    print(random_number, 'is not 6')