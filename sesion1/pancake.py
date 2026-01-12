"""Simple pancake sort using functions

Input: one line of integers separated by spaces (or commas)
Example: 3 6 1 5 2 4
"""

# read numbers from a single input line
def read_numbers():
    s = input('Enter numbers separated by space (or commas): ').replace(',', ' ').strip()
    numbers = s.split()
    x = []
    for nrStr in numbers:
        x.append(int(nrStr))
    return x

#Return the index of the maximum element in arr[0:size].
def find_max_index(arr, size):
    max_idx = 0
    i = 1
    while i < size:
        if arr[i] > arr[max_idx]:
            max_idx = i
        i += 1
    return max_idx

# pancake sort returns the list of flips and sorts in-place
def pancake_sort(arr):
    flips = []
    n = len(arr)
    curr_size = n
    while curr_size > 1:
        max_idx = find_max_index(arr, curr_size)

        if max_idx != curr_size - 1:
            if max_idx != 0:
                arr[:max_idx+1] = arr[:max_idx+1][::-1]
                flips.append(max_idx + 1)
            arr[:curr_size] = arr[:curr_size][::-1]
            flips.append(curr_size)

        curr_size -= 1

    return flips



def main():
    arr = read_numbers()

    flips = pancake_sort(arr)
    print('Sorted:', ' '.join(str(x) for x in arr))
    print('Flips:', ' '.join(str(x) for x in flips))


if __name__ == '__main__':
    main()