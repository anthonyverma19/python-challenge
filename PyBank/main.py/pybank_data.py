# Import required modules
import os
import csv

# Set path for file
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Define variables
total_months = 0
total_profit = 0
total_change = 0
prev_profit = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Calculate the totals
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])

        # Calculate the change in profit from the previous month
        current_profit = int(row[1])
        change = current_profit - prev_profit
        total_change = total_change + change
        prev_profit = current_profit

        # Calculate the greatest increase in profits
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change

        # Calculate the greatest decrease in profits
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

# Calculate the average change in profit
average_change = round(total_change / (total_months - 1), 2)

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export the results to a text file
output_path = os.path.join("financial_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
