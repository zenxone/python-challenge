import os
import csv

# Path to collect data from the Resources folder
# Set path for file "election_data.csv"
csvpath = os.path.join("C:/Users/james/pyCode/Resources/", "election_data.csv")

# Set path for output text file "e_analysis.txt"
txtoutpath = os.path.join("C:/Users/james/pyCode/Resources/", "e_analysis.txt")

# dataset is composed of three columns: Voter ID, County, and Candidate 
# Find the total number of votes cast
# Find the complete list of candidates who received votes
# Find the percentage of votes each candidate won
# Find total number of votes each candidate won
# Find winner of the election based on popular vote.

# Open the CSV and read header to access first actual row of data
# Initialize variables for calculations and storing results
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    totalVotes = 0
    Ccnt = 1
    LargestVote = 0
    electWinner = str()	
    candidates = []
    candidVote = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Loop through calculating total votes, and by conditional find each unique candidate append into list
    # Increment total vote for each candidate into a list with insert length determined by unique candidate list
    for row in csvreader:
        totalVotes = totalVotes + 1
        if str(row[2]) not in candidates:
           candidates.append(str(row[2]))
        for Ccnt in range(len(candidates)):
            if candidates[Ccnt] == str(row[2]):
               candidVote[Ccnt] = candidVote[Ccnt] + 1

# Print Election Results to terminal - All total votes, Each Candidate with their win percentage and total votes, then show election winner
# Print results to text file - All total votes, Each Candidate with their win percentage and total votes, then show election winner
# In midst of loop for printing to terminal and writing to text file determine candidate with largest vote, election winner
# open the text file "e_analysis.txt" using "write"
# writelines of text for each result into text file
with open(txtoutpath, "w", newline="") as textfile:
    textfile.writelines(f"Electon Results\r\n-------------------------\r\nTotal Votes: {totalVotes}\r\n-------------------------\r\n")
    print(f"\r\nElecton Results\r\n-------------------------\r\nTotal Votes: {totalVotes}\r\n-------------------------\r")

    for Ccnt in range(len(candidates)):
        if candidVote[Ccnt] > LargestVote:
           electWinner = candidates[Ccnt]
           LargestVote = candidVote[Ccnt]
        textfile.writelines(f"{candidates[Ccnt]}: {format(candidVote[Ccnt]/totalVotes*100,'.3f')}% ({candidVote[Ccnt]})\r\n")
        print(f"{candidates[Ccnt]}: {format(candidVote[Ccnt]/totalVotes*100,'.3f')}% ({candidVote[Ccnt]})")

    textfile.writelines(f"\r-------------------------\r\nWinner: {electWinner}\r\n-------------------------\r")		
print(f"\r-------------------------\r\nWinner: {electWinner}\r\n-------------------------\r")