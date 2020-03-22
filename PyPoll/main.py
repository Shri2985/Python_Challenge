
#----------------------------------------------------------------------------------------------------
# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# ------------------------------------------------------------------------------------------------------

# Importing the Dependencies 

import os
import csv

#Define the Variables

count_of_Votes = 0
Count_of_CandidateVote=0
Candidates={}
Candidatedict={}
# Assign the CSV File to the Variable
Election_csv = os.path.join('election_data.csv')

with open(Election_csv, 'r') as csvfile:
# # Read in the CSV file

    # Split the data on commas
    Election = csv.reader(csvfile, delimiter=',')
    if csv.Sniffer().has_header:
        next(Election)
    for row in Election:
        count_of_Votes += 1
        if row[2] in Candidates:
            Count_of_CandidateVote = Candidates[row[2]]
            Count_of_CandidateVote += 1
            Candidatedict = {row[2]:Count_of_CandidateVote}
            Candidates.update(Candidatedict)
        else:
            Count_of_CandidateVote= 1
            Candidatedict = {row[2]:Count_of_CandidateVote}
            Candidates.update(Candidatedict)
      
    print("Election Results")
    print("---------------------------------")
    print("Total Votes:  "+ str(count_of_Votes))
    print("---------------------------------")
    WinnerCandidateVote = 0
    WinnerDict = {}
    for row in Candidates:
        Count_of_CandidateVote = float(Candidates[row])
        if WinnerCandidateVote < Count_of_CandidateVote:
            WinnerCandidateVote = Count_of_CandidateVote
            WinnerDict.clear()
            WinnerDict = {row:WinnerCandidateVote}
        Percentage = Count_of_CandidateVote / count_of_Votes
        Percentage = Percentage * 100
        PercentageFormat = "{0:.3f}".format(Percentage)
        Candidate_Vote_Format = "{0:.0f}".format(Count_of_CandidateVote)
        print(row +": " + PercentageFormat + "% (" + Candidate_Vote_Format + ")")
    print("---------------------------------")

    for row in WinnerDict:
        print("Winner:  "+ row)

    print("---------------------------------")

 # Export the details to notepad
    outF =open("myOutFile.txt", "w")
    outF.write("\n")
    outF.write("Election Results")
    outF.write("\n")
    outF.write("---------------------------------")
    outF.write("\n")
    outF.write("Total Votes:  "+ str(count_of_Votes))
    outF.write("\n")
    outF.write("---------------------------------")
    outF.write("\n")
    for row in Candidates:
        Count_of_CandidateVote = float(Candidates[row])
        if WinnerCandidateVote < Count_of_CandidateVote:
            WinnerCandidateVote = Count_of_CandidateVote
            WinnerDict.clear()
            WinnerDict = {row:WinnerCandidateVote}
        Percentage = Count_of_CandidateVote / count_of_Votes
        Percentage = Percentage * 100
        PercentageFormat = "{0:.3f}".format(Percentage)
        Candidate_Vote_Format = "{0:.0f}".format(Count_of_CandidateVote)
        outF.write(row +": " + PercentageFormat + "% (" + Candidate_Vote_Format + ")")
        outF.write("\n")

    outF.write("---------------------------------")
    outF.write("\n")
    for row in WinnerDict:
        outF.write("Winner:  "+ row)
        outF.write("\n")
    outF.write("---------------------------------")

    outF.write("\n")
 
 
 
