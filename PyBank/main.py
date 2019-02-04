import os
import csv

csvpath = 'budget_data.csv'
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
  
    month_count = 0
    net_amount = 0
    averagechange = []

    for row in csvreader:
        month_count = month_count + 1
        net_amount = net_amount + int(row[1])
        
    
        
    
    print("Financial Analysis")
    print("-----------------------------------------")
    print("Total months:" + " " + str(month_count))
    print("Total:" + " " + "$" + str(net_amount))
  
       
    
