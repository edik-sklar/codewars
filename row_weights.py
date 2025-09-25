def row_weights(array):
    # Given an array of positive integers (the weights),
    # return a new array,
    # whereby the first one is the total weight of even,
    # and the second one is the total weight of odd.
    # Note that the array will never be empty.
    return [sum(array[::2]), sum(array[1::2])]

print(row_weights([50, 60, 70, 80]))