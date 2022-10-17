# The Goal for this assignment is to create a Python script that analyzes the records to calculate each of the following values:
# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in profits (date and amount) over the entire period
# 6. The final script should both print the analysis to the terminal and export a text file with the results.

# Dependencies
import os
import csv

# Here we Define the PyBank variables
Total_months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# Path to the resources folder to collect the data
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# This will open and read the csv file
with open(budget_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read through each row of data after the header
    for row in csv_reader:

    count_months += 1

    current_month_profit_loss = int(row[1])
    net_profit_loss += current_month_profit_loss









# print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# export a text file with the results
budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")