# usd = int('95')
# print(usd, type(usd))
# usd_number = 95
#
# n = 2.60
# print(type(n))


usd = input("Enter USD amount: ")
usd_number = float(usd)
exchange_rate = 102
bdt = usd_number * exchange_rate
# print(usd_number,'is equal to', bdt, 'bdt')
paragraph = str(usd_number) + ' is equal to ' + str(bdt) + ' BDT'
print(paragraph)