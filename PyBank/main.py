
#----------------------------------------------------------------------------------------------------
#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period
# ------------------------------------------------------------------------------------------------------

# Importing the Dependencies 

import os
import csv

#Define the Variables

count_of_months = 0
Net_Amount=0
Increase=0
Decrease=0
IncreaseDate=""
DecreaseDate=""

# Assign the CSV File to the Variable
Budget_csv = os.path.join('budget_data.csv')

with open(Budget_csv, 'r') as csvfile:

# # Read in the CSV file

    # Split the data on commas

    Budget = csv.reader(csvfile, delimiter=',')
    if csv.Sniffer().has_header:
        next(Budget)
    for row in Budget:
        count_of_months += 1
        Net_Amount += float(row[1])
        Average=Net_Amount/count_of_months
        if count_of_months == 1:
            Decrease = float(row[1])
            DecreaseDate= row[0]
        if float(row[1]) > Increase:
            Increase = float(row[1])
            IncreaseDate = row[0]
        if float(row[1]) < Decrease:
            Decrease = float(row[1])
            DecreaseDate = row[0]
    # print the Details to the console
          
    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months:  "+ str(count_of_months))
    print("Total: $"+str(Net_Amount))
    print("Average  Change: $"+str(Average))
    print("Greatest Increase in Profits:" + IncreaseDate +" " + str(Increase))
    print("Greatest Decrease in Profits:" + DecreaseDate + " "+str(Decrease))
    
 # Export the details to notepad
    outF =open("myOutFile.txt", "w")
    outF.write("\n")
    outF.write("Financial Analysis")
    outF.write("\n")
    outF.write("---------------------------------")
    outF.write("\n")
    outF.write("Total Months:  "+ str(count_of_months))
    outF.write("\n")
    outF.write("Total: $"+str(Net_Amount))
    outF.write("\n")
    outF.write("Average  Change: $"+str(Average))
    outF.write("\n")
    outF.write("Greatest Increase in Profits:" + IncreaseDate +" " + str(Increase))
    outF.write("\n")
    outF.write("Greatest Decrease in Profits:" + DecreaseDate + " "+str(Decrease))
    outF.write("\n")

    

    
   
 
 
