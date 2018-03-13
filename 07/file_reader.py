# allows you to access arguments passed to python files
import sys
# standard library for csv files
import csv
# filesystem lib to check if file exists
import os.path

# Read csv file and print data
def read_csv(csv_file):
    with open(csv_file) as csv_file:
        table = csv.DictReader(csv_file)
        for row in table:
            print 'Count Participants:', row['COUNT PARTICIPANTS'] 

## Try to read file and print Count Participants
## If invalid file is provided throw error
try:
    ## Save first argument to variable
    csv_file = sys.argv[1]
    
    ## Check if file exists
    ## Raise error if it doesn't
    if(os.path.isfile(csv_file)):
        read_csv(csv_file)
    else: 
        raise ValueError('Please provide valid file')
except Exception as error:
    #catch and print error
    print error

## Run in the terminal with this command
## python file_reader.py demopgrahic.py