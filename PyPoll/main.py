# The goal for is to create a Python script that analyzes the votes and calculates each of the following values:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. The final script should both print the analysis to the terminal and export a text file with the results.

# Dependencies
import os
import csv
import collections
from collections import Counter
voters_candidates = []
votes_per_candidate = []
election_data_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    for row in csv_reader:

        voters_candidates.append(row[2])

    sorted_list = sorted(voters_candidates)
    
    arrange_list = sorted_list

    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # The percentage of votes each candidate won
    for percentwon in votes_per_candidate:
       
        one1 = format((percentwon[0][1])*100/(sum(count_candidate.values())),'.3f')
        two2 = format((percentwon[1][1])*100/(sum(count_candidate.values())),'.3f')
        three3 = format((percentwon[2][1])*100/(sum(count_candidate.values())),'.3f')
        four4 = format((percentwon[3][1])*100/(sum(count_candidate.values())),'.3f')

    
# Print the analysis to the terminal
print("Election Results")
print("---------------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("---------------------------------")
print(f"{votes_per_candidate[0][0][0]}: {one1}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {two2}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {three3}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][3][0]}: {four4}% ({votes_per_candidate[0][3][1]})")
print("--------------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("--------------------------------")


# Export a text file with the results
election_file = os.path.join("..", "analysis", "election_data.txt")
with open(election_file, "w") as out_file:

    out_file.write("Election Results\n")
    out_file.write("--------------------------------\n")
    out_file.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    out_file.write("--------------------------------\n")
    out_file.write(f"{votes_per_candidate[0][0][0]}: {one1}% ({votes_per_candidate[0][0][1]})\n")
    out_file.write(f"{votes_per_candidate[0][1][0]}: {two2}% ({votes_per_candidate[0][1][1]})\n")
    out_file.write(f"{votes_per_candidate[0][2][0]}: {three3}% ({votes_per_candidate[0][2][1]})\n")
    out_file.write(f"{votes_per_candidate[0][3][0]}: {four4}% ({votes_per_candidate[0][3][1]})\n")
    out_file.write("--------------------------------\n")
    out_file.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    out_file.write("--------------------------------\n")    