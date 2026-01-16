'''
Greedy is an algorithm design technique that builds 
    a solution step by step by always choosing 
    the locally best option at each step, without revisiting past choices.
'''

'''
Task: 
    select the maximum number of non-overlapping meetings (classic scheduling)

Each meeting is (start_time, end_time). 
Greedy rule: always pick the meeting that finishes earliest.
'''

def sort_by_end_time(meetings):
    n = len(meetings)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if meetings[i][1] > meetings[j][1]:
                temp = meetings[i]
                meetings[i] = meetings[j]
                meetings[j] = temp


def greedy_schedule_max_meetings(meetings):
    sort_by_end_time(meetings)

    chosen = []
    last_end = -1

    for meeting in meetings:
        start = meeting[0]
        end = meeting[1]

        if start >= last_end:
            chosen.append(meeting)
            last_end = end

    return chosen


meetings = [
    (9, 10),
    (9, 12),
    (10, 11),
    (11, 13),
    (12, 14),
    (13, 15),
]

result = greedy_schedule_max_meetings(meetings)

print(result)
