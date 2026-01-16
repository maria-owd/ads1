'''
Pattern of reduction technique:
    - Transform the problem
    - Solve the known problem
    - Transform the answer back
'''

def hasDuplicates(arr):
    arr.sort()

    for i in range (0, len(arr)-2):
        if arr[i] == arr[i+1]:
            return True
        else:
            return False

arr = [22, 78, 22, 45, 78]
print(hasDuplicates(arr)) 