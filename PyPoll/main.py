#Import Dependencies

import csv
import os

#Set File Path

filepath = os.path.join ("Resources","election_data.csv")

#Define Lists

voter_id = []
county = []
candidate = []

#Read and output CSV skip header

with open (filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
        
#Transfer data into lists

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
     

    total_votes = sum(1 for row in voter_id)
    
set(candidate)
Candidates_Running = list(set(candidate))

#Count candidate votes and calculate percentage and assign to the following values:


#Li - "count_li" "li_per"
count_li = candidate.count("Li")
li_per = round((count_li*100/total_votes),3)

#O'Tooley - "count_otooley" "otooley_per"
count_otooley = int(candidate.count("O'Tooley"))
otooley_per = round((count_otooley*100/total_votes),3)

#Khan - "count_khan" "khan_per"
count_khan = int(candidate.count("Khan"))
khan_per = round((count_khan*100/total_votes),3)

#Correy - "count_correy" "correy_per"
count_correy = int(candidate.count("Correy"))
correy_per = round((count_correy*100/total_votes),3)

#Calculate winner from list and assign to value "Winner"

def counter(candidate):
    return max(set(candidate), key = candidate.count)

Winner = (counter(candidate))

#Print analysis summary

print(f"""
Election Results
--------------------------
Total Votes: {str(total_votes)}
--------------------------
Khan:     {str(khan_per)}% ({str(count_khan)})
Correy:   {str(correy_per)}% ({str(count_correy)})
Li:       {str(li_per)}% ({str(count_li)})
O'Tooley: {str(otooley_per)}% ({str(count_otooley)})
--------------------------
Winner: {str(Winner)}
--------------------------
""")

#Save analysis summary to text file in Analysis directory

with open("Analysis/pypollanalysis.txt", "a") as f:
    print(f"""
    Election Results
    --------------------------
    Total Votes: {str(total_votes)}
    --------------------------
    Khan:     {str(khan_per)}% ({str(count_khan)})
    Correy:   {str(correy_per)}% ({str(count_correy)})
    Li:       {str(li_per)}% ({str(count_li)})
    O'Tooley: {str(otooley_per)}% ({str(count_otooley)})
    --------------------------
    Winner: {str(Winner)}
    --------------------------
    """, file = f)
