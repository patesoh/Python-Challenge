import os
import csv

budget_csv_path = os.path.join("budget_data.csv")

months = 0
#list of date and profit-loss values respectively
date = []
pl = []

#difference/change month over month in profit/loss
difference = float(0)
total = 0
previous = float(0)
change = []



with open(budget_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
 
   #Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

    #loop through the table to get number of rows/months, calculate total net profit/loss, and get a list of dates and profit-loss values respectively    
    for row in csv_reader:
        months += 1
        total += 1
        date.append(str(row[0]))
        pl.append(float(row[1]))

        #calculate difference/change month over month and store in a list
        current = float(row[1])
        difference = (current - previous)
        change.append(float(difference))
        previous = current
        
        #difference to capture month over month changes
        
        
       
    #remove first value as the first difference value is the first value listed in the profit/loss column, couldnt figure out how to fix this above
    change.pop(0)
    #print(change) 
    #to ensure first value was removed

    #calculate net profit-loss (total), then calculate sum of changes month-over-month
    total = round(sum(pl))
    summom = sum(change)

    
   
    #Get 'best' and 'worst' date (MM-YY) info for greatest profit and greatest loss values captured in best and worst from pl list
    WorstDate = date[pl.index(max(pl))]
    BestDate = date[pl.index(min(pl))]

    #Divide sum of changes by (months - 1) because there will be one less value for the change relative to the number of months
    avg = round((summom/(months - 1)),2)
        
    #Get greatest increase and greatest decrease in change month-over-month and assign it to 'best' and 'worst' respectively, round to 2 decimal places for average
    best = round(max(change)) 
    worst = round(min(change))
    

    print(f"Financial Analysis")
    print("-----------------------------")
    print(f"Total months: {months}")
    print(f"Total: {total}")
    print(f"Average  Change: {avg}")
    print(f"Greatest Increase in Profits: {BestDate} (${best})")
    print(f"Greatest Decrease in Profits: {WorstDate} (${worst})")
    

# Specify the file to write to
output_path = os.path.join("Output", "Financial_Analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents,\r\n for appropriate format in notepad
with open(output_path, 'w', newline='\r\n') as txtfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    print("Financial Analysis  ", file=txtfile,)
    print(f"-----------------------------  ", file=txtfile,)
    print(f"Total months: {months}  ", file=txtfile,)
    print(f"Total: {total}  ", file=txtfile,)
    print(f"Average  Change: {avg}  ", file=txtfile,)
    print(f"Greatest Increase in Profits: {BestDate} (${best})  ", file=txtfile,)
    print(f"Greatest Decrease in Profits: {WorstDate} (${worst})  ", file=txtfile,)
