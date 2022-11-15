# normal_body_temp = 98.6
# temp = float(input('Enter your body Temperature: '))
#
# if temp > normal_body_temp:
#     print('Paracetamol 2 Bela')
# else:
#     print('Vitamin Tablet 3 Bela')

# Jalanta is an actor of Bangladesh. He is Nayok
# Rain is an actress of Bangladesh. She is Nayika


name = input('Enter Name: ')
gender = input('Enter Gender (m/f): ')
country = input('Enter Country Name: ')

# profession , pronoun, known_as

if gender == 'm':
    profession = 'actor'
    pronoun = 'He'
    known_as = 'nayok'
else:
    profession = 'actress'
    pronoun = 'She'
    known_as = 'Nayika'

print(f'{name} is an {profession} of {country}. {pronoun} is {known_as}')

