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
    
    for key, value in Name_Candidate.items():
        Percent_Candidate[key] = format((value/total_number_vote) * 100, ".3f")

    for key in Name_Candidate.keys():
        if Name_Candidate[key] > total_number_winner:
            Winner = key
            total_number_winner = Name_Candidate[key]

    print("Election Results")
    print("------------------------------------")
    print(f"Total Votes: {total_number_vote}")
    print("------------------------------------")
    for key, value in Name_Candidate.items():
        print(f"{key}: {Percent_Candidate[key]}% ({str(value)})")
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
    for key, value in Name_Candidate.items():
        text.write(f"{key}: {Percent_Candidate[key]}% ({str(value)})\n")
    text.write("------------------------------------\n")
    text.write(f"Winner: {Winner}\n")
    text.write("------------------------------------\n")



