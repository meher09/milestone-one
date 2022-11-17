years = [1988,3214,2022,2020,1956,1578]
i = 0

while i < len(years):
    if years[i] % 4 == 0:
        print(years[i], 'is leap year')
    i = i+1