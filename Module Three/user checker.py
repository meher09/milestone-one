user_name = 'aouwal'
password = '123456'

input_user = input('Enter username: ')
input_pass = input('Enter password: ')

# if input_user == user_name and input_pass == password:
#     print('You have successfully Login')
# else:
#     print('Some thing went wrong')

if input_user != user_name or input_pass != password:
    print('Some thing went wrong')
else:
    print('You have successfully Login')



