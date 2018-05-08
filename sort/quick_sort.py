def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

length = 10

import random
print('Input:')
arr = [random.randint(0, length) for x in range(length)]
print(arr)
print('Output:')
sorted_arr = quick_sort(arr)
print(sorted_arr)
