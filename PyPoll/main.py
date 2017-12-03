#!/usr/bIN/env python
"""This code analysis polling data and ouput the winner of an election based minority vote
INPUT: .csv file(s) column headers must include "Candiadate"
        Example header and data is shown below
            Voter ID,County,Candidate
             1405627,Harsaw,Vestal
OUTPUT: Individual candidate performance and election winner
        Sample output
        Election Results
            --------------------------
            Total Votes: 4324001
            --------------------------
            Vestal : 8.9 (385440)
            Torres : 8.2 (353320)
            Seth : 0.9 (40150)
            Cordin : 0.6 (24090)
            Khan : 51.3 (2218231)
            Correy : 16.3 (704200)
            Li : 11.4 (492940)
            O'Tooley : 2.4 (105630)
            --------------------------
            Winner: Khan
            --------------------------
Author: Monica Martin
Date: Nov 21, 2017
"""
import csv
import os
import timeit

#import sys
#Set file path and data files
start_time = timeit.default_timer()
FPATH = r'.'
FILENAMES = ["election_data_1.csv", "election_data_2.csv"]
#Set OUTPUT_FILE and write all terminal results to file
OUTPUT_FILE = open(os.path.join(FPATH, "ElectionResults.out"), 'w')
#sys.stdout = OUTPUT_FILE

#Define variables
CANDIDATE_LIST = [None] #['Vestal', 'Torres', 'Seth', 'Cordin']
TOTAL_VOTE = 0
MAX_PERCENT_VOTE = 0

for fn in FILENAMES:
#Loop through all FILENAMES
#Read csv into Dictionary
    INPUT_FILE = csv.DictReader(open(os.path.join(FPATH, fn)))
    #Loop through INPUT_FILE, perform election results analysis
    for row in INPUT_FILE:
        TOTAL_VOTE = TOTAL_VOTE + 1
        CANDIDATE = row.get('Candidate')

        if CANDIDATE_LIST[0] is None:
            CANDIDATE_LIST[0] = CANDIDATE
            TOTAL_VOTES = [0]
            PERCENT_VOTES = [0]

        elif CANDIDATE not in CANDIDATE_LIST:
            CANDIDATE_LIST.append(CANDIDATE)
            TOTAL_VOTES.append(0)
            PERCENT_VOTES.append(0)

       # for CANDIDATE in CANDIDATE_LIST:
        for [c, v] in enumerate(CANDIDATE_LIST):
            if CANDIDATE == v:
                TOTAL_VOTES[c] = int(TOTAL_VOTES[c] + 1)
            PERCENT_VOTES[c] = ((TOTAL_VOTES[c] / TOTAL_VOTE) * 100)
#Find the WINNER
WINNIN_CADIDATE, PERCENT_VOTE = max(list(zip(CANDIDATE_LIST, PERCENT_VOTES)), key=lambda item: item[1])

# Ouput Election Analysis Results
print('Election Results\n--------------------------\n')
print('Total Votes: %i \n--------------------------\n' % TOTAL_VOTE)
for [c, v] in enumerate(CANDIDATE_LIST):
    print('%s : %3.1f (%i)' % (v, PERCENT_VOTES[c], TOTAL_VOTES[c]))
print('\n--------------------------\nWinner: %s\n--------------------------' % WINNIN_CADIDATE)

print('Election Results\n--------------------------\n', file=OUTPUT_FILE)
print('Total Votes: %i \n--------------------------\n' % TOTAL_VOTE, file=OUTPUT_FILE)
for [c, v] in enumerate(CANDIDATE_LIST):
    print('%s : %3.1f (%i)' % (v, PERCENT_VOTES[c], TOTAL_VOTES[c]), file=OUTPUT_FILE)
print('\n--------------------------\nWinner: %s\n--------------------------' % WINNIN_CADIDATE, file=OUTPUT_FILE)
#Close OUTPUT_FILE
OUTPUT_FILE.close()
print('\n\nelapsed time: %.2fs' % (timeit.default_timer() - start_time))