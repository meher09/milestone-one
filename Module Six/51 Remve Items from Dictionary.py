car = {
    'brand': 'ford',
    'model': 'Mustang',
    'year':2010,
    'color':'Black'
}

# print(car.get('year'))
# car.update({'color':'Blue'})
car.pop('color')

print(car)
car.pop('year')
print(car)