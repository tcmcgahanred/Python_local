import os
import sys
from datetime import date
import pandas as pd
import numpy
import csv
import re

# function  to convert csv rows to dictionaries and then do a few data conversions:
# ignore empty lines somehow
# trying to make this is as light and easy to deal with as possible.
# this is ambitious

def prestoChango(f): # need a function to capture all the dictionary conversions, with input being each individual dictionary
   with open(f, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # ignore empty line 'if' or 'while not' statement here?
        brief_date = row.get("Date Signed")
        row[brief_name] = row.pop("Date Signed") # rename 'Date Signed' key to briefname 
        row.pop('id') # remove the 'id' key and it's contents (could also rename is with fieldname field in .dictreader)
        sid = row.get("SID")

        
        for dn in row:
            dn = row.get("DN") # (CN=MORIN JOSEPH,) so I need to find everything between the 'CN=' and the first ','
            cn = re.findall("CN=(\w+) ", dn) + re.findall(" (\w+),", dn) # "CN=(\.+)," # Get username. Keep only the 'CN' from the 'DN' key (LASTNAME FIRSTNAME)
            username = cn[1] + " " + cn[0]
            return username
        
        #completed_brief ="{} ({}) completed the {} on {}, which was reported on {}".format(username, sid, brief_name, brief_date, reported)
        
        
        print(row) # should be row
