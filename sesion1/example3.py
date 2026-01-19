'''
1. process_data(lines)
    Input: list of strings (already stripped of \n)

    A) Unique songs dictionary:
        A song is identified by (artist, title). 
        Keep only the first occurrence duration (they will be the same anyway in tests).

    B) For each artist:
        plays = total number of lines for that artist (including duplicates)
        unique_songs = number of distinct songs for that artist
        total_time = sum of durations over all plays for that artist (duplicates count)

    {
    "Imagine Dragons": (plays, unique_songs, total_time_seconds),
    "The Weeknd": (...),
    ...
    }
'''

def process_data(lines):
    for line in lines:
        artist = line[0]
        title = line[1]
        duration = line[2] 

        print(artist)
        print(title)
        print(duration) 
    

def read_data(fileName):
    clean_line = []
    with open(fileName, 'r') as fin:
        lines = fin.readlines()

        for line in lines:
            clean_line.append(line.strip()) 
            
    return clean_line


info = read_data("playlist3.txt")
d = process_data(info) 
print(d) 