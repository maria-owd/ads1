'''
- We want to sort a list of numbers
- At each step, we find the smallest element in the unsorted part
- We place it in the correct position at the front
- Repeat until the list is sorted
'''


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [64, 25, 12, 22, 11]
print(selection_sort(arr)) 