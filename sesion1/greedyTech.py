'''
Builds a solution step by step by always choosing 
    the locally optimal option without backtracking.
'''

def activity_selection(start, end):
    n = len(start)

    # sort activities by end time (simple selection sort)
    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            if end[j] < end[min_pos]:
                min_pos = j

        # swap start times
        start[i], start[min_pos] = start[min_pos], start[i]
        # swap end times
        end[i], end[min_pos] = end[min_pos], end[i]

    selected = []
    last_end = -1

    for i in range(n):
        if start[i] >= last_end:
            selected.append((start[i], end[i]))
            last_end = end[i]

    return selected


start = [1, 3, 0, 5, 8, 5]
end   = [2, 4, 6, 7, 9, 9]

print("the optimal activity schedule {}".format(activity_selection(start, end))) 

'''
- correctness: correct due to greedy-choice property and optimal substructure.
- time complexity: Θ(n log n) due to sorting
- space complexity: Θ(1)
- remarks: does not always guarantee optimality for all problems.
'''
