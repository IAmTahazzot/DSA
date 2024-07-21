"""
Problem: Write a function called same, which accepts two arrays The function should return true if every value in the array has it's corrensponding value squared in the second arra. The frequency of values must be the same.

Example:

same([1, 2, 3], [4, 1, 9]) // true
same([1, 2, 3], [1, 9]) // false
same([1, 2, 1], [4, 4, 1]) // false (must be same frequency)
"""

# NEW: Frequency counting pattern


def same(array_one, array_two):
    # safe length check
    if not len(array_one) == len(array_two):
        return False

    dict_one = {}
    dict_two = {}

    # make array_one squared to match array_two
    array_one = [n**2 for n in array_one]

    # fill the dict
    for index in range(0, len(array_one)):
        # array_one to dict_one
        array_one_number = array_one[index]
        dict_one[array_one_number] = (
            dict_one.get(array_one_number) and dict_one.get(array_one_number) + 1
        ) or 1

        # array_two to dict_two
        array_two_number = array_two[index]
        dict_two[array_two_number] = (
            dict_two.get(array_two_number) and dict_two.get(array_two_number) + 1
        ) or 1

    # match them
    for key in dict_one:
        if not dict_one.get(key) == dict_two.get(key):
            return False

    return True


print(same([1, 2, 3], [4, 1, 9]))
print(same([1, 2, 3], [1, 9]))
print(same([1, 2, 1], [4, 4, 1]))
