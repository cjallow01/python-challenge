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

# PyBank variables
Total_months = []
profit_loss_changes = []

months_count = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# Path to the resources folder to collect the data
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# This will open and read the csv file
with open(budget_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in csv_reader:
        months_count += 1
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss
        if(months_count == 1):

            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue
        else:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            Total_months.append(row[0])

            profit_loss_changes.append(profit_loss_change)
            previous_month_profit_loss = current_month_profit_loss

    # Profit/Losses over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(months_count - 1), 2)

    # highest/lowest changes Profit/Losses over the entire period
    top_change_amount = max(profit_loss_changes)
    low_change_amount = min(profit_loss_changes)

    highest_month_index = profit_loss_changes.index(top_change_amount)
    lowest_month_index = profit_loss_changes.index(low_change_amount)

    # Assign Greatest increase and decrease month
    greatest_increase_month = Total_months[highest_month_index]
    greatest_decrease_month = Total_months[lowest_month_index]


# print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {months_count}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {greatest_increase_month} (${top_change_amount})")
print(f"Greatest Decrease in Profits:  {greatest_decrease_month} (${low_change_amount})")


# export a text file with the results
budget_file = os.path.join("..", "analysis", "budget_data.txt")
with open(budget_file, "w") as out_file:

    out_file.write("Financial Analysis\n")
    out_file.write("----------------------------\n")
    out_file.write(f"Total Months:  {months_count}\n")
    out_file.write(f"Total:  ${net_profit_loss}\n")
    out_file.write(f"Average Change:  ${average_profit_loss}\n")
    out_file.write(f"Greatest Increase in Profits:  {greatest_increase_month} (${top_change_amount})\n")
    out_file.write(f"Greatest Decrease in Profits:  {greatest_decrease_month} (${low_change_amount})\n")