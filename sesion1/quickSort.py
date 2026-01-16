'''
Quick Sort is a sorting algorithm based on the partition technique 
    that selects a pivot element and rearranges the array 
    so that all elements smaller than the pivot are placed before it 
    and all elements larger than the pivot are placed after it
    the sorting is performed during the partition step.
'''

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp

    return i + 1 


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)



data = [7, 2, 9, 4, 1, 6]
quick_sort(data, 0, len(data) - 1)

print(data)
