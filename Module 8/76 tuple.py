def area_volume(length, width, height):
    """
    return area and volume of any object
    """
    area = length * width
    volume = length * width * height
    return area, volume, length, width


test = area_volume(2,3,4)
print(test)
# print(test[-1])
test_list = list(test)
# print(test_list)
test_list[0] = 9
test_tup = tuple(test_list)
print(test_tup)


fruits = ("apple", "banana", "cherry")
x, y, z = fruits
print(y)