import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from datetime import datetime
from operator import itemgetter


def find_csv():
    for file in os.listdir(os.getcwd()):
        if file.endswith(".csv"):
            return os.path.join(os.getcwd(), file)


def read_csv(file_path):
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        rows = sorted(reader, key=itemgetter(9))
    del rows[-1]  # Remove header
    return rows


def get_axis(rows):
    dates = list()
    costs = list()
    num_ignored = 0
    prev_month = None
    for row in rows:
        try:
            price = float(row[8].replace(",","."))
        except ValueError:
            print('Warning: Cannot read price in: %s' % row)
            num_ignored += 1
            continue
        if price == 0:
            print('Warning: Missing price in: %s' % row)
            num_ignored += 1
            continue
        try:
            date = datetime.strptime(row[9], '%Y-%m-%d')
        except ValueError:
            try:
                date = datetime.strptime(row[9], '%Y-%m-00')  # Day missing
            except ValueError:
                print('Warning: Missing purchase date in: %s' % row)
                num_ignored += 1
                continue
        month = date.month
        if not prev_month:
            dates.append(date.strftime('%Y-%b'))
            costs.append(price)
        else:
            if month == prev_month:
                costs[len(costs) - 1] += price
            else:
                dates.append(date.strftime('%Y-%b'))
                costs.append(price)
        prev_month = month
    if num_ignored > 0:
         print('Ignored games %d of %d' % (num_ignored, len(rows)))
    return dates, costs


def plot_graph(x, y):
    index = np.arange(len(x))
    plt.title('Monthly expenditure of the collection (%d in total)' % np.sum(y))
    plt.xlabel('Month')
    plt.ylabel('Expenditure')
    bar = plt.bar(index, y)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%d' % int(height), ha='center', va='bottom')
    plt.xticks(index, x, rotation=30)
    mean = np.mean(y)
    mean_line = plt.axhline(mean, color='r', linestyle='--')
    mean_legend = 'Mean (%d)' % mean
    plt.legend([mean_line], [mean_legend])
    plt.show()


def main():
    if len(sys.argv) == 1:
        file_path = find_csv()
    else:
        file_path = sys.argv[1]
    rows = read_csv(file_path)
    dates, costs = get_axis(rows)
    plot_graph(dates, costs)


main()
