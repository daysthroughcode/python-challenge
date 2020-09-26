#!/usr/bin/env python
# coding: utf-8

#Import Dependencies

import csv
import os

#set path for object

filepath = os.path.join("Resources", "budget_data.csv")

#set lists

pnl = []
date = []

#read and output csv

with open (filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header
    
    csvheader = next(csvreader)
       
#split data into separate list

    for row in csvreader:
        date.append(row[0])
        pnl.append(row[1])
        
#calculate number of months

pl_months = len(date)

#change values to integers in pnl list

pnl = [int(i) for i in pnl]

#calculate sum in pnl list

pl_total = sum (pnl)

#define mean calculation function

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length
    
#calulate mean and round to two decimal places

pl_mean = round(average(pnl),2)

#Zip lists into a dictionary

rejoined_data = dict(zip(date,pnl))

#calculate greatest profit

gprofit = max(rejoined_data.items(), key = lambda x : x[1])

#calculate lowest profit

lprofit = min(rejoined_data.items(), key = lambda x : x[1])

#print 
    
print(f"""
Financial Analysis
------------------
Total Months: {str(pl_months)}
Total: {str(pl_total)}
Average Change: {str(pl_mean)}
Greatest Increase in Profits: {str(gprofit)}
Greatest Decrease in Profits: {str(lprofit)}
""")


#export multi line text. Open file, write and close at the end.

with open("Analysis/pybankanalysis.txt", "a") as f:

    print(f"""
    Financial Analysis
    ------------------
    Total Months: {str(pl_months)}
    Total: {str(pl_total)}
    Average Change: {str(pl_mean)}
    Greatest Increase in Profits: {str(gprofit)}
    Greatest Decrease in Profits: {str(lprofit)}
    """, file = f)


