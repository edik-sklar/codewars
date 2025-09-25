#Given a list of digits, return the smallest number that could be formed from these digits,
# using the digits only once (ignore duplicates).
# Only positive integers in the range of 1 to 9 will be passed to the function.

def min_value(digits):
    # choosing to use sort() inplace, it returns None instead of the sorted list assigned to a var
    digits.sort()
    #converting list to a string and returning int type
    return int("".join([str(i) for i in set(digits)]))

print(min_value([1, 9, 3, 1, 7, 4, 6, 6, 7]))