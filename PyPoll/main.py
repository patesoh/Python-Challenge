import os
import csv

election_csv_path = os.path.join("election_data.csv")

#create dictionary to hold key and values 
election = {}

#variable to count total number of votes 
total = 0


with open(election_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
 
   #skip the header row
    csv_header = next(csvfile)

    # loop through the table, assign candidate column as key in the election dictionary so as to identify unique candidate names and then add to the vote count every time that name appears again  
    for row in csv_reader:
        total += 1
        if row[2] in election.keys():
            election[row[2]] += 1
        else:
            election[row[2]] = 1

print(f'Election Results')
print(f'--------------------------')
print(f'Total Votes: {total}')
print(f'--------------------------')
for key, value in election.items():
    print(f'{key}: {round((value/total * 100),3)}% ({value})')
print(f'--------------------------')
print(f'Winner: '+ max(election, key=election.get))
print(f'--------------------------')

# Specify the file to write to
output_path = os.path.join("Output", "Election Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents,\r\n for appropriate format in notepad
with open(output_path, 'w', newline='\r\n') as txtfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    print(f'Election Results',file=txtfile)
    print(f'-------------------------',file=txtfile)
    print(f'Total Votes: {total}',file=txtfile)
    print(f'-------------------------',file=txtfile)
    for key, value in election.items():
        print(f'{key}: {round((value/total * 100),3)}% ({value})',file=txtfile)
    print(f'-------------------------',file=txtfile)
    print(f'Winner: '+ max(election, key=election.get),file=txtfile)
    print(f'-------------------------',file=txtfile)