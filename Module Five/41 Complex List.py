person_one = ['Moris',
              'male',
              'australia',
              '29th January 1988',
              'moris@jon.com',
              '01-0716-1221'
              ]

person_two = [
            'Vasko',
              'male',
              'Ukrain',
              '29th October 1956',
              'vasko@mon.com',
              '11-0716-1221'
]


gender = person_one[1]
if gender == 'male':
    relative = 'his'
    pronoun = 'he'
else:
    relative = 'her'
    pronoun = 'she'


sentence = f'{person_one[0]} is born {person_one[2].title()}. {relative.title()} date of birth is {person_one[3]}. {pronoun.title()} is available at {person_one[4]} and phone no is {person_one[-1]}'

print(sentence)
