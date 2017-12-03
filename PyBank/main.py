#!/usr/bin/env python3
"""
Author: Monica Martin
Date:   Nov-2017    

Input: csv files

Usage: Python3 main.py <filename1 filename2 ...>

Output: Financial Analysis
Sample Output:

Financial Analysis
------------------
Total Months:  41
Total Revenue: $18971412
Average Revenue Change: $-6758
Greatest Increase in Revenue: Jan-16 ($1837235)
Greatest Decrease in Revenue: Jul-14 ($-1779747)
"""

import csv
import os
import sys

def main(FILENAMES):
    FPATH = os.getcwd()
    OUTPUT_FILE = open(os.path.join(FPATH, "FinancailAnalysis.out"), 'w')
    

    for fn in FILENAMES:
        REV_LIST = []
        #Loop through all FILENAMES
        #Read csv into Dictionary
        reader = csv.DictReader(open(fn, 'r'))
        #Sort orderd Dictionary. Output is a list of ordered dictionary
        DATA_SORTED =(sorted(reader, key=lambda d: d['Date'].split(sep='-')[1]))

        #Store all revenue in a list
        for item in range(0,len(DATA_SORTED),1):
            REV_LIST.append(int(DATA_SORTED[item]['Revenue']))

        #Perform Financial Analysis
        TOTAL_REVENUE = sum(REV_LIST)
        DELTA_REV = [REV_LIST[i+1]-REV_LIST[i] for i in range(len(REV_LIST)-1)]
        AVE_CHNG = sum(DELTA_REV)/len(DELTA_REV)
        MAX_REVENUE_IN = max(DELTA_REV)
        MAX_REVENUE_RED = min(DELTA_REV)

        #Match Dates of max-min Revenue change 
        MAX_REVENUE_DATE = DATA_SORTED[DELTA_REV.index(MAX_REVENUE_IN)]['Date']
        MAX_REVENUE_RED_DATE = DATA_SORTED[DELTA_REV.index(MAX_REVENUE_RED)]['Date']

        print()
        # Ouput Financial Analysis
        print('Financial Analysis\n------------------')
        print("Total Months:  %s" % len(REV_LIST))
        print("Total Revenue: $%i" % TOTAL_REVENUE)
        print('Average Revenue Change: $%i' % int(AVE_CHNG))
        print('Greatest Increase in Revenue: %s ($%s)' % (MAX_REVENUE_DATE, MAX_REVENUE_IN))
        print('Greatest Decrease in Revenue: %s ($%s)' % (MAX_REVENUE_RED_DATE, MAX_REVENUE_RED))

        print('',file=OUTPUT_FILE)
        print('Financial Analysis\n------------------', file=OUTPUT_FILE)
        print("Total Months:  %s" % len(REV_LIST), file=OUTPUT_FILE)
        print("Total Revenue: $%i" % TOTAL_REVENUE, file=OUTPUT_FILE)
        print('Average Revenue Change: $%i' % int(AVE_CHNG), file=OUTPUT_FILE)
        print('Greatest Increase in Revenue: %s ($%s)' % (MAX_REVENUE_DATE, MAX_REVENUE_IN), \
            file=OUTPUT_FILE)
        print('Greatest Decrease in Revenue: %s ($%s)' % (MAX_REVENUE_RED_DATE, MAX_REVENUE_RED), \
            file=OUTPUT_FILE)

    OUTPUT_FILE.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <filename1 filename2 ...>\n\
          minimum of one filename required')
    else:
        FILENAMES=sys.argv[1:]
        main(FILENAMES)
