def sum_list(arr):
    if not arr: # Base Case
        return 0
    return arr[0] + sum_list(arr[1:])
print(f"Sum of [10, 20, 30]: {sum_list([10, 20, 30])}")