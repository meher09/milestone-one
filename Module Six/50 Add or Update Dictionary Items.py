# post = {
#     'id': 100,
#     'title': 'This is awesome title',
#     'content': 'These are awesome contents',
#     'author': 'Awesome Name',
#     'category': 'Awesome',
#     'slug':'awesome-title',
# }
#
# # post['sticky'] = True
# post.update({'sticky': True})
# print(post)

car = {
    'name': 'Toyota',
    'year': 2000,
}

car['year'] = 2002
print(car)
car.update({'color':'Yellow'})
print(car)
print(car.get('color'))
print(car['name'])