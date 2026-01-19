'''
We want to sort a list of numbers
We compare neighboring elements
If they are in the wrong order, we swap them
Bigger elements gradually move to the end
Repeat until sorted 
'''

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [5, 1, 4, 2, 8]
print(bubble_sort(arr)) 