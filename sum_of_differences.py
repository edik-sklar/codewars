# to sum the differences between consecutive pairs in the array in descending order.

def sum_of_differences(arr):
    list_of_sums = 0
    for i in range(-1, -len(arr), -1):
        list_of_sums += (arr[i] - arr[i-1])

    return list_of_sums


# List comprehension version
# def sum_of_differences(arr):
#     return sum(arr[i] - arr[i-1] for i in range(-1, -len(arr), -1))


print(sum_of_differences([1, 2, 10]))
