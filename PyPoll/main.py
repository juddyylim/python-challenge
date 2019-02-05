import os
import csv

csvpath = 'election_data.csv'
f = open("PyPoll.txt", "w")

def finalprint(text):
    f.write(text + "\n")
    print(text)

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) 

    votetotal = 0
    candidates = []
    votecount = []
    candidatevotes = []
    
    for row in csvreader:
        votetotal = votetotal + 1
        votecount.append(row[2])
        
        if row[2] not in candidates:
            candidates.append(row[2])
            candidatevotes.append(0)

    for x in range(len(votecount)):
        if votecount[x] == candidates[0]:
            candidatevotes[0] = candidatevotes[0] + 1
        elif votecount[x] == candidates[1]:
            candidatevotes[1] = candidatevotes[1] + 1
        elif votecount[x] == candidates[2]:
            candidatevotes[2] = candidatevotes[2] + 1
        elif votecount[x] == candidates[3]:
            candidatevotes[3] = candidatevotes[3] + 1
        else:
            pass

    def percentage(candidate):
        return '{0:.3%}'.format((candidate / len(votecount)))
    
    c1percent = percentage(candidatevotes[0])
    c2percent = percentage(candidatevotes[1])
    c3percent = percentage(candidatevotes[2])
    c4percent = percentage(candidatevotes[3])
    
    list = []
    for x in range(len(candidates)):
        list.append({"name": candidates[x], "votes": candidatevotes[x]})

    highestvote = 0
    winner = ""
    for x in range(len(list)):
        if list[x]["votes"] > highestvote:
            highestvote = list[x]["votes"]
            winner = list[x]["name"]
    
    finalprint("Election Results")
    finalprint("--------------------------")
    finalprint("Total Votes: " + str(votetotal))
    finalprint("--------------------------")
    finalprint(str(candidates[0]) + ": " + str(c1percent) + " " + "(" + str(candidatevotes[0]) + ")")
    finalprint(str(candidates[1]) + ": " + str(c2percent) + " " + "(" + str(candidatevotes[1]) + ")")
    finalprint(str(candidates[2]) + ": " + str(c3percent) + " " + "(" + str(candidatevotes[2]) + ")")
    finalprint(str(candidates[3]) + ": " + str(c4percent) + " " + "(" + str(candidatevotes[3]) + ")")
    finalprint("--------------------------")
    finalprint("Winner: " + winner)

