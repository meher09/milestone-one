person = [
    ['Moris','male','australia','1988','moris@jon.com'],
    ['Vasko','male','Ukrain','1956','vaso@jon.com'],
    ['Amni','female','Norway','1926','amni@jamni.com'],
    ['James','male','Bangladesh','1966','james@jamni.com'],
    ['Andrew','male','India','1985','andy@sandy.com'],
]

i = 0
while i < len(person):
    single_person = person[i]
    name = single_person[0]
    gender = single_person[1]
    country = single_person[2]
    birth_year = single_person[3]
    email = single_person[4]
    if gender == 'male':
        pronoun = 'he'
        relative = 'his'
    else:
        pronoun = 'she'
        relative = 'her'

    sentence = f'{name.title()} lives in {country}.{pronoun.title()} was born in {birth_year}. {relative} email address is {email}'
    print(sentence)
    i = i+1
    # print(name, gender,country, birth_year, email, sep="---")







