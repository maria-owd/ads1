'''
Incrementally builds a sorted array by inserting each element into its correct position.
'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key 
    
    return arr 

arr = [5, 1, 9, 3, 4]

print("sorted array {}".format(insertion_sort(arr))) 

'''
- correctness -> invariant: after iteration i, subarray a[0..i] is sorted.
- time complexity: Θ(n²) worst-case, Θ(n) best-case
- space complexity: Θ(1)
- remarks: stable and in-place.
'''