# import os module
import os

# import csvfile
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

def pybank(budget_data):
    Data = int(budget_data[0])
    Profit_loss = int(budget_data[1])

    total_month = 0

    total_month = total_month + 1

print(f'total number of months {total_month}')


# reading csv file
with open(csvpath, newline = "") as pybank:
    csvreader = csv.reader(pybank, delimiter = ",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

