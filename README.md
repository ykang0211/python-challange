# import os module
import os

# import csvfile
import csv

csvpath = os.path.join("Resources", "election_data.csv")

Voter_ID = []
County = []
Candidate = []
Name_Candidate = {}
Percent_Candidate = {}
total_number_vote = 0
total_number_winner = 0

# open csv

with open(csvpath, newline = "") as pypoll:
    csvreader = csv.reader(pypoll, delimiter = ",")

    csv_header = next(csvreader)
    # print(csvreader)
    # print(f"CSV Header : {csv_header}")
    for row in csvreader:
        
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        # print(Candidate)
        # total number of Votes
        total_number_vote = total_number_vote + 1
        if row[2] in Name_Candidate.keys():
            Name_Candidate[row[2]] = Name_Candidate[row[2]] + 1
        else:
            Name_Candidate[row[2]] = 1
    
    for row[2], value in Name_Candidate.items():
        # this function gives .000
        Percent_Candidate[row[2]] = format((value/total_number_vote) * 100, ".3f")
        
        # this function gives .0 eventhough I try 2, 3, or 4 for rounding decimal
        # Percent_Candidate[row[2]] = round((value/total_number_vote) * 100, 2)

    for row[2] in Name_Candidate.keys():
        if Name_Candidate[row[2]] > total_number_winner:
            Winner = row[2]
            total_number_winner = Name_Candidate[row[2]]

# print solutions

    print("Election Results")
    print("------------------------------------")
    print(f"Total Votes: {total_number_vote}")
    print("------------------------------------")
    for row[2], value in Name_Candidate.items():
        print(f"{row[2]}: {Percent_Candidate[row[2]]}% ({int(value)})")
    print("------------------------------------")
    print(f"Winner: {Winner}")
    print("------------------------------------")

# write pypoll in text

with open("csvpath.text", "w", newline = "") as text:
    text.write("\n")
    text.write("Election Results\n")
    text.write("------------------------\n")
    text.write(f"Total Votes: {total_number_vote}\n")
    text.write("------------------------------------\n")
    for row[2], value in Name_Candidate.items():
        text.write(f"{row[2]}: {Percent_Candidate[row[2]]}% ({int(value)})\n")
    text.write("------------------------------------\n")
    text.write(f"Winner: {Winner}\n")
    text.write("------------------------------------\n")

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
