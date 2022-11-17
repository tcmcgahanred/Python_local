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
import glob

# IGNORE: sys.path.append('C:/Users/timot/Documents/Python_local/python_projects/presto.py')

# see end of file for DataFrame example. That's what the new brief file looks like that's used to update the master


cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))


### iterate over the brief files (e.g. LOAC, JFAM, etc) in that directory (KM will need to manually rename the file for now)
# the flow would be to iterate over the files, get their respective name, run prestoChango against the file, and then export all the updates to the master brief .txt. Later, 
# another function will print out information based on input provided by Mission Planners (e.g. SID and brief name)

directory = 'C:\\Users\\timot\Documents\\Python_local\\python_projects'
 
def briefFiles(directory):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)

briefFiles(directory)            

# make the file object accessible to the next group/function

### get file names so that we can replace the 'Date Signed' column. This'd then indicate that the brief was completed on the date in that cell/row. # note: I'll need a directory iterator here so I don't have to hardcode in file names like this OR just the input variables at the end of the file
#use file objects from previous functions to parse out name of each file, apart from the path.

#path = 'C:\\Users\\timot\\Documents\\Python_local\\python_projects\\example_excel\\LOAC_20221105.xlsx'

bfs = briefFiles(directory)

def fileName(bfs):
    file_name = os.path.basename(path).split('/')[-1] # get file name from path. Can this be combined with the below?
    brief_name = re.findall('\w{3,4}', file_name)[0] # Parse out the brief name from the file name. (e.g. LOAC) Can this be combined with the above?
    return brief_name

fileName(bfs)

#Only prints 'LOAC'. Really need to learn how to iterate AND print all the output.

##############################EXPERIMENT#####################################################

directory = 'C:\\Users\\timot\Documents\\Python_local\\python_projects'
 
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        for brief in directory:
            brieflist = []
            file_name = os.path.basename(filename).split('/')[-1] 
            #brief_name = re.findall('\w{3,4}', file_name)[0]
            brief_name = re.findall("(LOAC)|(JFAM)|(UAUP)", file_name)
            #brieflist.write(brief_name))
            print(brief_name)
    else:
        print("Not a file")
        
        
        re.findall("LOAC | JFAM | UAUP", cwd)



    


lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')


###############################################################################################################

# make brief_name accessible to prestoChango


### convert excel to csv. csvs are the only practical way to convert rows, in the format they're in from the webapp, into dictionaries. Pandas doesn't make it too easy.
# can delete the csvs after, if necessary
# I'd like to do WITHOUT pandas so I don't require that dependency for myself or other users. Also, not even sure it's an option on 'the network'.

brief_xlsx = pd.read_excel('C:\\Users\\timot\Documents\\Python_local\\python_projects\\LOAC_20221105.xlsx') 
briefTocsv = brief_xlsx.to_csv('C:\\Users\\timot\\Documents\\Python_local\\python_projects\\LOAC_20221105.csv', index = None, header=True)
brief_csv = 'C:\\Users\\timot\\Documents\\Python_local\\python_projects\\LOAC_20221105.csv'

### function to convert csv rows to dictionaries and then do a few data conversions, inevitably formatting as strings to be printed to a text file:
# Also, was working on making this a stand-alone module that I'd call into this program

def prestoChango(brief_csv): # need a function to capture all the dictionary conversions, with input being each individual dictionary
   with open(brief_csv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # ignore empty row 'if' or 'while not' statement here?
        brief_date = row.get("Date Signed")
        row[brief_name] = row.pop("Date Signed") # rename 'Date Signed' key to brief_name 
        row.pop('id') # remove the 'id' key and it's contents b/c it's useless (could also rename is with fieldname field in .dictreader)
        sid = row.get("SID")
        
        # seems like these next three should be grouped as a separate for, but not sure
        dn = row.get("DN") # (CN=MORIN JOSEPH,) so I need to find everything between the 'CN=' and the first ','
        cn = re.findall("CN=(\w+) ", dn) + re.findall(" (\w+),", dn) # "CN=(\.+)," # Get username. Keep only the 'CN' from the 'DN' key (LASTNAME FIRSTNAME)
        username = cn[1] + " " + cn[0]
        
        reported = date.today()
        completed_brief ="{} ({}) completed the {} brief on {}, which was reported on {}".format(username, sid, brief_name, brief_date, reported)
        # print(completed_brief) # prints all the contents of the csv, but can't get this to the text file, WHICH IS WHERE I'M STUCK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #return completed_brief # returns just the first row
    return completed_brief # returns just the last row
   with open('C:\\Users\\timot\\Documents\\Python_local\\python_projects\\Brief_Master_20221102.txt', 'a') as f:
    f.write(completed_brief + '\n')

prestoChango(brief_csv) # GAH! Need to iterate over every row in the csvfile and append that to the text file!!!!!!!!!!!!!!!!!!!!!!!!!!!! HOW?!? Change the structure of the function somehow!?! use range() or a while loop?

##############################EXPERIMENT#####################################################

# experiement on recursive version here

def prestoChango(brief_csv): 
   with open(brief_csv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    update_brief = []
    for row in reader:
        print("do a thing once")
   with open('C:\\Users\\timot\\Documents\\Python_local\\python_projects\\test.txt', 'a') as f:
    f.write(completed_brief + '\n')

prestoChango(brief_csv) 






###############################################################################################################



### add todays date to the title of the new master brief tracker (maybe the text document)

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
