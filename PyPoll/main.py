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

with open(csvpath, newline = "") as pypoll:
    csvreader = csv.reader(pypoll, delimiter = ",")

    csv_header = next(csvreader)
    # print(csvreader)
    # print(f"CSV Header : {csv_header}")
    for row in csvreader:
        
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

        # total number of Votes
        total_number_vote = total_number_vote + 1
        if row[2] in Name_Candidate.keys():
            Name_Candidate[row[2]] = Name_Candidate[row[2]] + 1
        else:
            Name_Candidate[row[2]] = 1
    
    for row[2], value in Name_Candidate.items():
        Percent_Candidate[row[2]] = format((value/total_number_vote) * 100, ".3f")

    for row[2] in Name_Candidate.keys():
        if Name_Candidate[row[2]] > total_number_winner:
            Winner = row[2]
            total_number_winner = Name_Candidate[row[2]]

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



