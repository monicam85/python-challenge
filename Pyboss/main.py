'''
Author:
Date: 11/21/2017
Revision: -
'''
import os
import re
import csv
import time
from tkinter import filedialog
from tkinter import Tk
from tkinter import messagebox
from us_state_abbrev import *

def main():
    CUR_DIR = os.getcwd()
    root = Tk()
    root.withdraw()
    global start_time


    messagebox.showinfo( \
	   message='Please select input file(s). Use CTRL+Click to select multiple file', \
           default='ok', title='Information')
    # select file using file browser GUI
    FILENAME_PATH =  filedialog.askopenfilenames(initialdir=CUR_DIR, title="Select file", filetypes=(("Comma Seperated Value Files","*.csv"),("all files","*.*")))
    FILENAME_PATH = (list(FILENAME_PATH))

    for fn in FILENAME_PATH:
        # split string containing full path and filename
        FILENAME_PATH_SPLIT = fn.split(sep = '/')
        # define OUTPUT filename for FILENAME_PATH_SPLIT
        FILENAME, EXT = (FILENAME_PATH_SPLIT[len(FILENAME_PATH_SPLIT) - 1]).split(sep = '.')
        # append .out file extension. OUT = [orignal filename].out
        OUT = os.path.join(CUR_DIR, FILENAME + '.out')
        start_time= time.process_time()
        with open(fn, 'r', newline = '' ) as INPUT_FILE:
                READER_csv = csv.DictReader(INPUT_FILE)
                with open(OUT, 'w', newline = '' ) as OUTPUT_FILE:
                    WRITER_csv = csv.DictWriter(OUTPUT_FILE, fieldnames = READER_csv.fieldnames)
                    WRITER_csv.writeheader()
                    for row in READER_csv:
                        #Update/reformat the current dictionary
                        ROW_UPDATED=row.copy()
                        ROW_UPDATED['Name'] = re.sub(' ', ',', ROW_UPDATED['Name'], count = 1, flags = 0)
                        ROW_UPDATED['DOB'] = '/'.join(i for i in ROW_UPDATED['DOB'].split(sep='-')[::-1])
                        ROW_UPDATED['SSN'] = re.sub(r'[0-9]{3}-[0-9]{2}', '***-**', ROW_UPDATED['SSN'], count = 0, flags = 0)
                        ROW_UPDATED['State'] = list(us_state_abbrev.keys())[list(us_state_abbrev.values()).index(row['State'])]

                        #Write updated dictionert to output file
                        WRITER_csv.writerow(ROW_UPDATED)


if __name__ == "__main__":
    main()
    Elasped=time.process_time()-start_time
    print('Elasped time: %f' % (Elasped))