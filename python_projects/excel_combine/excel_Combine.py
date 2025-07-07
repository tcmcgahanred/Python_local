from asyncore import file_dispatcher

# pip install openpyxl
# pip install pandas


import os
import sys
from datetime import date
import pandas as pd
import numpy
import csv
import re
#import presto as pr
import importlib

# vsys.path.append('C:/Users/timot/Documents/Python_local/python_projects/presto.py')

# get file names so that we can replace the 'Date Signed' column. This'd then indicate that the brief was completed on the date in that cell/row. # note: I'll need a directory iterator here so I don't have to hardcode in file names like this OR just the inupt variables

path = 'C:\\Users\\timot\\Documents\\Python_local\\python_projects\\example_excel\\LOAC_20221105.xlsx'
file_name = os.path.basename(path).split('/')[-1] # Can this be combined with the below?
file_name # can be removed later 
brief_name = re.findall('\w{3,4}', file_name)[0] # Can this be combined with the above?
brief_name # can be removed later

# convert excel to csv

brief_xlsx = pd.read_excel('C:\\Users\\timot\Documents\\Python_local\\python_projects\\LOAC_20221105.xlsx') 
briefTocsv = brief_xlsx.to_csv('C:\\Users\\timot\\Documents\\Python_local\\python_projects\\LOAC_20221105.csv', index = None, header=True)
brief_csv = 'C:\\Users\\timot\\Documents\\Python_local\\python_projects\\LOAC_20221105.csv'

# function  to convert csv rows to dictionaries and then do a few data conversions:

def prestoChango(brief_csv): # need a function to capture all the dictionary conversions, with input being each individual dictionary
   with open(brief_csv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    update_brief = []
    for row in reader:
        # ignore empty line 'if' or 'while not' statement here?
        brief_date = row.get("Date Signed")
        row[brief_name] = row.pop("Date Signed") # rename 'Date Signed' key to briefname 
        row.pop('id') # remove the 'id' key and it's contents (could also rename is with fieldname field in .dictreader)
        sid = row.get("SID")
        dn = row.get("DN") # (CN=MORIN JOSEPH,) so I need to find everything between the 'CN=' and the first ','
        cn = re.findall("CN=(\w+) ", dn) + re.findall(" (\w+),", dn) # "CN=(\.+)," # Get username. Keep only the 'CN' from the 'DN' key (LASTNAME FIRSTNAME)
        username = cn[1] + " " + cn[0]
        reported = date.today()
        completed_brief ="{} ({}) completed the {} brief on {}, which was reported on {}".format(username, sid, brief_name, brief_date, reported)
        print(completed_brief) # should be row
        #return update_brief
    #return completed_brief
   with open('C:\\Users\\timot\\Documents\\Python_local\\python_projects\\Brief_Master_20221102.txt', 'a') as f:
    f.write(completed_brief + '\n')

prestoChango(brief_csv) # GAH! Need to iterate over every row in the csvfile and append that to the text file!!!!!!!!!!!!!!!!!!!!!!!!!!!! HOW?!? Change the structure of the function somehow!?! use range() or a while loop?







# add todays date to the title of the new master brief tracker (maybe the text document)

reported = date.today() # I'd like to format this with the date/time so everytime the script is ran, it'd update the title with the time too
print("Today's date:", today)


# This would be a seperate script, BUT, I'd like for users to be asked for the SID and a brief name and then print out all dictionaries/entries with those two keys. What'd be even better is to print out only the distinct briefs with the highest dates. Need to figure that out. We'll start with 
 

sid_request = str(input("Enter a SID "))
brief_request = str(input("Enter a brief name: LOAC, JFAM, or SAF"))








########################## DataFrame format ############################

pd.read_excel(path)

""" pd.read_excel(path)
       id      SID                           DN       LOAC
0  123456   jmorin   CN=MORIN JOSEPH, THING=xxx 2022-10-01
1  789123  ftorres  CN=TORRES FABIAN, THING=xxx 2022-10-02
2  456789  choggle  CN=HOGGLE CHANCE, THING=xxx 2022-10-03 """
