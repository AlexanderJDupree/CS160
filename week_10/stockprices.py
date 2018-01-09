import csv

def main():
    with open('nike.csv', 'r') as f:
        file = csv.DictReader(f)
        totals = [float(line['Adj Close']) for line in file]
        average = sum(totals) / len(totals)
        f.seek(0, 0)
        next(file)
        max_high_low = max(
            [abs(float(line['High']) - float(line['Low'])) for line in file])
        f.seek(0, 0)
        next(file)
        max_open_close = max(
            [abs(float(line['Close']) - float(line['Open'])) for line in file])


    print("Average Close: {0:.3f}".format(average))
    print("Highest Close: {0:.3f}".format(max(totals)))
    print("Largest spread between Open and Close in one day: {0:.3f}"
        .format(max_open_close))
    print("Largest spread between High and Low in one day: {0:.3f}"
        .format(max_high_low))

main()
