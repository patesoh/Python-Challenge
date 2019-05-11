import os
import csv

employee_csv_path = os.path.join("employee_data.csv")

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#lists to store emp id, first name, last name, dob, ssn and state  
empid=[]
firstname=[]
lastname=[]
birthdate=[]
ssn=[]
state=[]


with open(employee_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
 
   # skip the header row
    csv_header = next(csvfile)

    # loop through the table, assign data using the 'split' feature to the appropriate lists
    for row in csv_reader:
        empid.append(row[0])
        firstname.append((row[1]).split(" ")[0])
        lastname.append((row[1]).split(" ")[1])
        birthdate.append(row[2])
        ssn.append('***-**-' + row[3].split("-")[2])
        state.append(us_state_abbrev[row[4]])

#zip the lists together
employee_data=zip(empid,firstname,lastname,birthdate,ssn,state)

# Specify the file to write to
output_path = os.path.join("Output", "EmployeeData-PyBoss.csv")

# Open the file using "write" mode. Specify the variable to hold the contents,\r\n for appropriate format in notepad
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Add a row containing the headers
    csvwriter.writerow(["Employee ID", "First Name", "Last Name", "Date of Birth", "Social Security No.","State"])
    
    # Add data stored in the lists to this new file
    csvwriter.writerows(employee_data)
    