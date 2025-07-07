

# pip install openpyxl
# pip install pandas

import os
import sys
from datetime import date
import pandas as pd
import numpy
import csv
import re
import importlib
import glob

excel_files = 'C:\\Users\\timot\\Documents\\python\\Python_local\\python_projects\\Master_Folder\\Example_excel'

#cwd = os.getcwd()

def prestoConverto(excel_files):
    for file in excel_files:
        brief_xlsx = pd.read_excel(file)
        fileconvert = brief_xlsx.to_csv(brief_xlsx, index=None, header=True) 
        return fileconvert

brief_csv = prestoConverto(excel_files)

print(brief_csv)


for file_path in brief_files:
    brief_name = briefName(file_path)


def briefName(file):
    file = os.path.basename(file).split('/')[-1]
    brief_name = re.findall('(LOAC|JFAM|UAUP)', file)[0]
    return brief_name

briefName(file)

def briefFiles(directory):
    found_files = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            found_files.append(f)
    return found_files

briefFiles(directory)  

brief_files = briefFiles(directory)


def prestoChango(brief_name, brief_csv): # need a function to capture all the dictionary conversions, with input being each individual dictionary
   with open(brief_csv, newline='') as csvfile:
        with open('C:\\Users\\timot\\Documents\\Python_local\\python_projects\\Brief_Master_20221102.txt', 'a') as f:
            reader = csv.DictReader(csvfile)
            for row in reader:
            # ignore empty row 'if' or 'while not' statement here?
                brief_date = row.get("Date Signed")
                row[brief_name] = row.pop("Date Signed") # rename 'Date Signed' key to brief_name
                row.pop('id') # remove the 'id' key and it's contents b/c it's useless (could also rename is with fieldname field in .dictreader)
                sid = row.get("SID")
                dn = row.get("DN") # (CN=MORIN JOSEPH,) so I need to find everything between the 'CN=' and the first ','
                cn = re.findall("CN=(\w+) ", dn) + re.findall(" (\w+),", dn) # "CN=(\.+)," # Get username. Keep only the 'CN' from the 'DN' key (LASTNAME FIRSTNAME)
                username = cn[1] + " " + cn[0]
                reported = date.today()
                completed_brief ="{} ({}) completed the {} brief on {}, which was reported on {}\n".format(username, sid, brief_name, brief_date, reported)
            f.write(completed_brief)


prestoChango(brief_name, file_path)

prestoChango(brief_csv)