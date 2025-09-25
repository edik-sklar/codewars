
def sum_of_differences(arr):
    arr = sorted(arr, reverse=True)
    return sum(arr[i] - arr[i+1] for i in range(len(arr)-1)) if len(arr) > 1 else 0



print(sum_of_differences([1, 2, 10]))
