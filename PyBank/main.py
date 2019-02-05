import os
import csv

csvpath = 'budget_data.csv'
f = open("PyBank.txt", "w")

def finalprint(text):
    f.write(text + "\n")
    print(text)

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
  
    month_count = 0
    net_amount = 0
    date = []
    profitloss = []
    change = []

    for row in csvreader:
        month_count = month_count + 1
        net_amount = net_amount + int(row[1])
        date.append(row[0])
        profitloss.append(int(row[1]))

    for x in range(0, len(profitloss)-1):
        change.append(int(profitloss[x+1]) - int(profitloss[x]))

    averagechange1 = profitloss[len(profitloss)-1] - profitloss[0]
    averagechange = (round(averagechange1/(len(profitloss) - 1), 2))
    
    increase = max(change)
    decrease = min(change)

    row1 = change.index(increase)
    row2 = change.index(decrease)
    date1 = date[row1 + 1]
    date2 = date[row2 + 1]
    
    finalprint("Financial Analysis")
    finalprint("-----------------------------------------")
    finalprint("Total months:" + " " + str(month_count))
    finalprint("Total:" + " " + "$" + str(net_amount))
    finalprint("Average Change:" + " " + "$" + str(averagechange))
    finalprint("Greatest Increase in Profits:" + " " + str(date1) + " " + "$" + str(increase))
    finalprint("Greatest Decrease in Profits:" + " " + str(date2) + " "+ "$" + str(decrease))
    
    
