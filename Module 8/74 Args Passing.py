def add(a,b):
    """
    return total of two numbers
    """
    total = a+b
    return total
#
#
# print(add(2,3))

def mulitple_add(*args):
    total = 0
    for number in args:
        total += number
    return total


result = mulitple_add(1,2,3,4,5,6,7,8,9,10,11)
print(result)
