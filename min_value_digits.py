# Given a list of digits, return the smallest number that could be formed from these digits,
# using the digits only once (ignore duplicates).
# Only positive integers in the range of 1 to 9 will be passed to the function.

def min_value(digits):
    set_digits = set(digits)
    # list creates a temp list, need to assign to a var
    digit_list = list(set_digits)
    # choosing to use sort() inplace, it returns None instead of the sorted list assigned to a var
    digit_list.sort()
    # converting a list to a string and returning an int type
    return int("".join([str(i) for i in digit_list]))


print(min_value([4, 8, 1, 4]))
