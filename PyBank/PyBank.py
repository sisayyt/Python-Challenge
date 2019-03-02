import csv
import os


# file path
data = os.path.join("..", "Resources", "Budget.csv")

#  month and revenue 
months = []
revenue = []

#reading csv file
with open(data, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))

#total months
total_months = len(months)

#calculating revenue increase, revenue decrease, and total revenue   
greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0

#loop through data to find revenue increase and decline 
for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]

#Average revenue 
average_change = round(total_revenue/total_months, 2)

#sets path for output file
output_dest = os.path.join("..", "Resources", 'pybank_output.txt')

# Printing the summary
with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

#Printing to the terminal
with open(output_dest, 'r') as readfile:
    print(readfile.read())
