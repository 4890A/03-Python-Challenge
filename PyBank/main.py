""" Analyzes profit/loss data for a bank """

import csv
import os


csvpath = os.path.join("budget_data.csv")


def main():
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)  # remove header

        # initilize variables to be used in the loop
        month_count = 0
        greatest_inc = 0.0
        greatest_dec = 0.0
        total = 0.0
        profit_loss = []
        dates = []
        changes = []

        for row in csvreader:

            month_count += 1  # increment a month
            total += float(row[1])  # add to toal
            profit_loss.append(float(row[1]))  # add prfoit to list
            dates.append(row[0])  # append date to another list

        # find the differences between two dates, starting with the second date
        for i in range(1, len(profit_loss)):

            # append change
            change = profit_loss[i] - profit_loss[i - 1]
            changes.append(change)

            # check if change is greater/smaller than greatest change
            if change > greatest_inc:
                greatest_inc = change
                greatest_inc_date = dates[i]  # save date if true

            if change < greatest_dec:
                greatest_dec = change
                greatest_dec_date = dates[i]

        avg_change = sum(changes) / len(changes)  # calculate average change

        output = open("output.txt", "w")  # load txt file to write to
        result = (
            "Financial Analysis \n"
            + "------------------------- \n"
            + f"Total Months: {month_count} \n"
            + f"Total: ${total:.2f} \n"
            + f"Average Change: ${avg_change:.2f}\n"
            + (
                f"Greatest Increase in Profits: "
                + f"{greatest_inc_date} (${greatest_inc:.2f}) \n"
            )
            + (
                f"Greatest Decrease in Profits: "
                + f"{greatest_dec_date} (${greatest_dec:.2f}) \n"
            )
        )

        print(result)
        print(result, file=output)  # export results to .txt file

    return None


main()
