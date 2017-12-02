#!/usr/bIN/env python
"""Monica MartIN
"""
import csv
import os
#import sys
#Set file path and data files
FPATH = r'.\HW_Assignments\HW3\PyBank'
FILENAMES = ["budget_data_1.csv", "budget_data_2.csv"]
#Set OUTPUT_FILE and write all terminal results to file
OUTPUT_FILE = open(os.path.join(FPATH, "FinancailAnalysis.out"), 'w')
#sys.stdout = OUTPUT_FILE
#Define variables
REVENUE = 0
MAX_REVENUE_IN = 0
MAX_REVENUE_RED = 0
COUNT = 0
TOTAL_REVENUE = 0
MAX_REVENUE_DATE = None
AVG_REVENUE = 0

for fn in FILENAMES:
#Loop through all FILENAMES
#Read csv into Dictionary
    INPUT_FILE = csv.DictReader(open(os.path.join(FPATH, fn)))
    #Loop through INPUT_FILE, perform financial analysis calculation
    for row in INPUT_FILE:
        REVENUE = int(row["Revenue"])
        COUNT = COUNT + 1
        TOTAL_REVENUE = TOTAL_REVENUE + REVENUE
        if MAX_REVENUE_IN == 0 or MAX_REVENUE_IN < REVENUE:
            MAX_REVENUE_IN = REVENUE
            MAX_REVENUE_DATE = row["Date"]
        elif MAX_REVENUE_RED == 0 or REVENUE < MAX_REVENUE_RED:
            MAX_REVENUE_RED = REVENUE
            MAX_REVENUE_RED_DATE = row["Date"]
# Ouput Financial Analysis
print('Financial Analysis\n------------------')
print("Total Months:  %s" % COUNT)
print("Total Revenue: $%i" % TOTAL_REVENUE)
print('Average Revenue Change: $%i' % int(TOTAL_REVENUE / COUNT))
print('Greatest Increase in Revenue: %s ($%s)' % (MAX_REVENUE_DATE, MAX_REVENUE_IN))
print('Greatest Decrease in Revenue: %s ($%s)' % (MAX_REVENUE_RED_DATE, MAX_REVENUE_RED))

#Close OUTPUT_FILE
print('Financial Analysis\n------------------', file=OUTPUT_FILE)
print("Total Months:  %s" % COUNT, file=OUTPUT_FILE)
print("Total Revenue: $%i" % TOTAL_REVENUE, file=OUTPUT_FILE)
print('Average Revenue Change: $%i' % int(TOTAL_REVENUE / COUNT), file=OUTPUT_FILE)
print('Greatest Increase in Revenue: %s ($%s)' % (MAX_REVENUE_DATE, MAX_REVENUE_IN), \
    file=OUTPUT_FILE)
print('Greatest Decrease in Revenue: %s ($%s)' % (MAX_REVENUE_RED_DATE, MAX_REVENUE_RED), \
    file=OUTPUT_FILE)

OUTPUT_FILE.close()
