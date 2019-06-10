""" """
import os
import csv


def get_results(tally, candidates):

    results = "Election Results\n--------------------- \n"
    total = sum(tally)  # sum subtotals for each candidate
    results += f"Total Votes: {total}"
    results += "\n--------------------------"

    for i in range(len(candidates)):
        name = candidates[i]
        percent = f"{(tally[i]/total) * 100:.2f}"
        statement = f"{name}: {percent} ({tally[i]})"
        results += "\n" + statement

    winner = candidates[tally.index(max(tally))]
    results += "\n--------------------------"
    results += "\nWinner: " + winner
    results += "\n--------------------------"

    return results


csvpath = os.path.join("election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    votes = []
    for row in csvreader:
        votes.append(row[2])

    candidates = list(set(votes))  # convert to set to get unique set
    tally = [0] * len(candidates)  # zeros list to hold tallys for candidates

    # tally up votes by matching name in vote to candidate
    for name in votes:
        tally[candidates.index(name)] += 1

    # sort results by most votes first
    tally, candidates = zip(*sorted(zip(tally, candidates), reverse=True))
    results = get_results(tally, candidates)
    print(results)

    output = open("output.txt", "w")
    print(results, file=output)
