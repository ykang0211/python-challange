# import os module
import os

# import csvfile
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

Date = []
profit_loss = []
number_months = 0
total_profit_loss = 0
average_profit_loss = 0

average_change = []
previous_change = 0



# reading csv file
with open(csvpath, newline = "") as pybank:
    csvreader = csv.reader(pybank, delimiter = ",")

    # print(csvreader)

    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    for row in csvreader:
        
        # append date and profit/loss to list
        Date.append(row[0])
        profit_loss.append(row[1])
        # print(type(row[1]))

        # calculate total months
        number_months = number_months + 1

        # calculate total profit/loss
        total_profit_loss = total_profit_loss + int(row[1])


        # calculate average profit/loss
        average_profit_loss = total_profit_loss / number_months

        # average = sum((int(profit_loss)) / len(profit_loss)
        monthly_change = int(row[1]) - previous_change
        previous_change = int(row[1])

        average_change.append(monthly_change)

        average = sum(average_change) / number_months
      

        greatest_in = max(average_change)
        date_increase = Date[average_change.index(greatest_in)]
        greatest_de = min(average_change)
        date_decrease = Date[average_change.index(greatest_de)]

        
    print(" ")
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {number_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${average_profit_loss}")
    print(f"Greatest Increase in Profits: {date_increase} (${greatest_in})")
    print(f"Greatest Decrease in Profits: {date_decrease} (${greatest_de})")
    # print(f"Average Change: ${average}")

with open("csvpath.text", "w", newline = "") as text:
    text.write("\n")
    text.write("Financial Analysis\n")
    text.write("------------------------\n")
    text.write(f"Total Months: {number_months}\n")
    text.write(f"Total: ${total_profit_loss}\n")
    text.write(f"Average Change: ${average_profit_loss}\n")
    text.write(f"Greatest Increase in Profits: {date_increase} (${greatest_in})\n")
    text.write(f"Greatest Decrease in Profits: {date_decrease} (${greatest_de})\n")