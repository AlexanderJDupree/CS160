# file:animalVideos_adupree.py
# description: Outputs the average, longest, and shortest video length
# author: Alexander DuPree
# date: 12/02/2017
# compiler: Python 3.6

from textwrap import dedent

def main():
    longest, shortest, average = find_min_max("animalVideos.csv")
    output(longest, shortest, average)


def find_min_max(filename):
     with open(filename, 'r') as f:
        next(f) # Skips fieldnames
        file = [line.split(',') for line in f.readlines()]
        longest = [vid for vid in file if int(vid[2]) == max(int(l[2]) for l in file)]
        shortest = [vid for vid in file if int(vid[2]) == min(int(l[2]) for l in file)]
        average = sum([int(vid[2]) for vid in file ]) / len(file)
        return longest[0], shortest[0], average

def output(longest, shortest, average):
    print(dedent("""
        Longest Video: {}
        Shortest Video: {}
        Average Video Length: {}
        """.format(longest[0], shortest[0], average)))

main()
