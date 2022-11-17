# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years or salary greater than 20000.
# Ask user for their salary and year of service and print the net bonus amount.

salary = int(input('Enter your salary: '))
years_of_services = float(input('Enter years of services: '))

if years_of_services > 5 or salary >= 20000:
    bonus = 0.05
    net_salary = salary + salary * bonus
    print('Your net salary with bonus',net_salary)
else:
    print('You get only your salary',salary, 'USD')


