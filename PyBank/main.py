import os
import csv

# Path to collect data from the Resources folder
# Set path for file "budget_data.csv"
csvpath = os.path.join("C:/Users/james/pyCode/Resources/", "budget_data.csv")

# Set path for output file
txtoutpath = os.path.join("C:/Users/james/pyCode/Resources/", "f_analysis.txt")

# Define the function and have it accept the 'budget_data' as its sole parameter
# dataset is composed of two columns: Date and Profit/Losses
# Find the total number of months
# Find the total net amount of "Profit/Losses" over the entire period
# Find the average change in "Profit/Losses" between months over the entire period
# Find the greatest increase in profits (date and amount) over the entire period
# Find the greatest decrease in losses (date and amount) over the entire period

# Open the CSV and read header to access first actual row of data
# Initialize variables for calculations and storing results
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    greatestIncr = 0
    greatestDecr = 0
    totalMonths = 0
    totalProfitLoss = 0
    totalChg = 0
    incrMonth = str()
    decrMonth = str()	

    # Loop through calculating total months, total profit loss, total change to calculate average
    # and by conditionals find greatest increase in profits with specific month, greatest decrease in profits with specific month
    for row in csvreader:
        totalMonths = totalMonths + 1
        totalProfitLoss = int(row[1]) + totalProfitLoss

        if totalMonths > 1:
            totalChg = (int(row[1])) - priorPL + totalChg			

            if (int(row[1])) - priorPL >= 0 and greatestIncr < ((int(row[1])) - priorPL):
                greatestIncr = (int(row[1])) - priorPL
                incrMonth = str(row[0])
            elif (int(row[1])) - priorPL < 0 and greatestDecr > ((int(row[1])) - priorPL):
                greatestDecr = (int(row[1])) - priorPL
                decrMonth = str(row[0])
			
        priorPL = int(row[1])

# Print results to terminal - Total Months, Total Win-Loss, Average Change, Greatest Profit Increase, Greatest Profit Decrease
print(f"\r\nFinancial Analysis\r\n---------------------------\r")
print(f"Total Months: {totalMonths}")		
print(f"Total: ${totalProfitLoss}")
print(f"Average Change: ${round(totalChg/(totalMonths-1),2)}")
print(f"Greatest Increase in Profits: {incrMonth} $({greatestIncr})")
print(f"Greatest Decrease in Profits: {decrMonth} $({greatestDecr})")

# Print results to text file - Total Months, Total Profits, Average Change, Greatest Profit Increase, Greatest Profit Decrease
#open the file "f_analysis.txt" using "write"
#writelines of text for each result into text file
with open(txtoutpath, "w", newline="") as textfile:

    textfile.writelines(f"Financial Analysis\r\n---------------------------\r\n")	  
    textfile.writelines(f"Total Months: {totalMonths}\r\n")
    textfile.writelines(f"Total: ${totalProfitLoss}\r\n")
    textfile.writelines(f"Average Change: ${round(totalChg/(totalMonths-1),2)}\r\n")
    textfile.writelines(f"Greatest Increase in Profits: {incrMonth} (${greatestIncr})\r\n")
    textfile.writelines(f"Greatest Decrease in Profits: {decrMonth} (${greatestDecr})\r\n")