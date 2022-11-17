user_one = ['MohnDoe', 32, False, 'Andaman']
#               0         1     2       3
#               -4        -3    -2      -1
# print(user_one[0], user_one[-4], sep='-----')
# print(user_one[1], user_one[-3], sep='-----')
# print(user_one[3], user_one[-1], sep='------')
#
# partial_list = user_one[:3]
# print(partial_list)

# John Doe is a man of 26 years old. he lives in kamruk kamakkha
name = user_one[0]
age = user_one[1]
living_place = user_one[3]
is_male = user_one[2]
if is_male:
    pronoun = 'he'
    gender = 'man'
else:
    pronoun = 'she'
    gender = 'woman'

sentence = f'{name} is a {gender} of {age} years old. {pronoun.upper()} lives in {living_place}'

print(sentence)
