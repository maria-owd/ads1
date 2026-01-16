'''
Patern for interleaving sort (merge sort):
    - split array into 2 halves
    - sort each of them
    - interleave (merge) them back in order
'''

def mergeSort(arr):
    print ("\nsorting", arr)
    if len(arr) <= 1:
        print("\ttoo small, return")
        
        return arr
    
    mid = len(arr) // 2
    print ("\t mid=",mid)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    print ("merging ", left, right)

    return merge(left, right) 

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

arr = [7, 2, 9, 4, 1, 6] 
print(mergeSort(arr)) 
