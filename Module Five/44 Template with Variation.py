import random
person = ['Moris','Chittagong']
name = person[0]
location = person[1]

sentence_one_group = [
    f'This is {name}',
    f'My name is {name}',
    f'{name} is my name',
]

sentence_two_group = [
    f'I live in {location}',
    f'I reside in {location}',
    f'I was raised in {location}',
    f'{location} is place where i reside',
]

sentence_one = random.choice(sentence_one_group)
sentence_two = random.choice(sentence_two_group)

paragraph = f'{sentence_one}. {sentence_two}'

print(paragraph)
