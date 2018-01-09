# file: data_mining_adupree.py
# description: Return average and largest spreads in csv file
# author: Alexander DuPree
# date: 11/29/2017
# compiler: Python 3.6

from textwrap import dedent

def main():
    with open('nike.csv', 'r') as f:
        next(f)
        file = f.readlines()
        file = [line.split(',') for line in file]
        totals = [float(line[6]) for line in file]
        average = sum(totals) / len(totals)
        max_high_low = max([abs(float(line[2]) - float(line[3])) for line in file])
        max_open_close = max([abs(float(line[4]) - float(line[1])) for line in file])


    print(dedent("""
        Average Close: {0:.3f}
        Highest Close: {1:.3f}
        Largest spread between Open and Close in one day: {2:.3f}
        Largest spread between High and Low in one day: {3:.3f}
        """.format(average, max(totals), max_open_close, max_high_low)))

main()
