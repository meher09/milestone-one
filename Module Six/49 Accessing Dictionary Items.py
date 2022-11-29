user = {
    'id':1,
    'first_name': 'Jalanta',
    'last_name':'Khalil',
    'username': 'admin',
    'password': '123456789',
    'role':'admin',
}

# first_name = user['first_name']
# last_name = user['last_name']
# print(first_name,last_name)

# first_name = user.get('first_name')
# print(first_name)

keys = user.keys()
values = user.values()
print(list(keys))
print(list(values))