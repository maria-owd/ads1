'''
- Each task has a start and end time
- Only one task at a time can be chosen
- Goal: maximize the number of tasks
- Sort tasks by end time
- Always choose the task that finishes earliest
- Then choose the next task that starts after the last chosen one ends
'''


def select_activities(a):
    # sort activities by end time
    a.sort(key=lambda x: x["e"])

    s = [0]          # indices of selected activities
    k = 0            # last selected index in s

    for i in range(1, len(a)):
        if a[i]["b"] >= a[s[k]]["e"]:
            s.append(i)
            k += 1

    return s


# example
activities = [
    {"b": 1, "e": 4},
    {"b": 3, "e": 5},
    {"b": 0, "e": 6},
    {"b": 5, "e": 7},
    {"b": 8, "e": 9},
    {"b": 5, "e": 9},
]

print(select_activities(activities))
