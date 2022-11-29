users = [
{
    'username':'ananta',
    'password':'rain',
    'role': 'admin'
},


{
    'username': 'Sakhib Kan',
    'password': 'googlyApu',
    'role':'contributor'
}

]

for user in users:
    print(user.get('username'))