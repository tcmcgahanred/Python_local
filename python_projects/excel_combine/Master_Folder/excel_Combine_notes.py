# SUDOOOOOOOO

#COA 1###########################################################################################################################################

# iterate through CWD for master_brief_tracker_YYYYMMDD.xlsx
# if master_brief_tracker_YYYYMMDD.xlsx does not exist, then do the following:
# iterate through ARCHIVE and copy last master_brief_tracker_YYYYMMDD.xlsx to CWD !!! TAKE CARE this may be dangerous !!!

# iterate through CWD for master_brief_tracker_YYYYMMDD.xlsx

# if master_brief_tracker_YYYYMMDD.xlsx exists, then do the following:
# iterate through CWD for briefname_YYYYMMDD.xlsx

# if briefname_YYYYMMDD.xlsx date (e.g. LOAC_20221102) is less than master_brief_tracker_YYYYMMDD.xlsx date, then do nothing

# if briefname_YYYYMMDD.xlsx date (e.g. LOAC_20221102) is equal to or greater than master_brief_tracker_YYYYMMDDxlsx date, then do the following:

#### function A ###

# open/read briefname_YYYYMMDD.xlsx
# iterate through each axis 0 (row) and axis 1 (column) for SID and dates


# if file is briefname_YYYYMMDDxlsx and SID exists and date is greater than but not equal to previous date, .replace() with greater date
# if file is briefname_YYYYMMDD.xlsx and SID exists and date is equal to or less than existing date, do nothing
# if file is briefname_YYYYMMDD.xlsx and SID exists and date does not exist, write in date
# if file is briefname_YYYYMMDD.xlsx and SID does not exists, write in date axis 0 (row)


#### function B ###

# COA 1 plus this #

# read brief file
# interate for regex of SID
# read master file
# interate fro regex of SID
# bool for exists and if so, matches SIDs
# if doesn't exist, append to end of file
# if exists bool for greater date between files
# if brief file has greater date, overwrite master date
# if brief file has lesser date, do nothing



#### function C ###

#open file
# pull rows if axis 0 / axis 1 is greater than a particular number/date and then add that ?
#if .xlsx title 'LOAC', copy rows/column D to rows/column G
# might use .concat() here

# maybe this is the way
# but we'll concat contents of the file onto the axis 1 based on the file name, in it's respective order. (e.g. )

# maybe just uses a series of if statements for axis o and axis 1 matches to overwrite a value? Using pandas.DataFrame.replace?
# could use regex substitution (e..g re.sub(regexstring, data) or re.findall(regexstring, data))


#COA 3###########################################################################################################################################


# uses re.findall() / pd.series() / .replace()

import os
import sys
import pandas as pd
import numpy

# Concatenation function with axis=0 stacks the first DataFrame over the second:

mbrief = pd.DataFrame({'a': [1,3,6,8,9], 'b': ['red', 'green', 'blue', 'white', 'black']})
new_brief = pd.DataFrame({'a': [0,2,4,5,7], 'b': ['jun', 'jul', 'aug', 'sep', 'oct']})
pd.concat([mbrief, new_brief], axis=1)





pd.read_excel(r'C:\Users\timot\OneDrive\Documents\Cyber_Security\References\Python\example_excel\example3.xlsx', "Sheet1", usecols=[0, 2, 3]) 
pd.read_excel(r'C:\Users\timot\OneDrive\Documents\Cyber_Security\References\Python\example_excel\example3.xlsx', "Sheet1", usecols="C:E") 

old = pd.DataFrame({'A': [1, 2, 3]})
new = pd.DataFrame({'B': [4, 5, 6]})
#is a dictionary, call keys or value

new.get('A')


s1 = pd.Series(['a', 'b']) # Usually, in Python, one-dimensional structures are displayed as a row of values. On the contrary, here we see that Series is displayed as a column of values.
s2 = pd.Series(['c', 'd'])
pd.concat([s1, s2])


new.get('A')


srs_a = pd.Series([10,30,60,80,90])
srs_b = pd.Series(['red', 'green', 'blue', 'white' 'black'])
df = pd.DataFrame({'a': srs_a, 'b': srs_b}) # changed series into a DF by specifying the axis 1 (e.g. column 'a' and 'b'), whereas before, the series only has the axis 0 (e.g. the indexes)

df



srs_a = pd.Series([1,3,6,8,9])
srs_b = pd.Series(['red', 'green', 'blue', 'white', 'black'])
df = pd.DataFrame({'a': srs_a, 'b': srs_b})
df.loc[2, 'b'] # To access an element within DataFrame we need to provide two indexes (one per each axis). Also, instead of bare brackets, we need to use .loc method
df.loc[3, 'a']

Concatenation function with axis=0 stacks the first DataFrame over the second:

df1 = pd.DataFrame({'a': [1,3,6,8,9], 'b': ['red', 'green', 'blue', 'white', 'black']})
df2 = pd.DataFrame({'a': [0,2,4,5,7], 'b': ['jun', 'jul', 'aug', 'sep', 'oct']})
pd.concat([df1, df2], axis=1)



s = pd.Series([1, 2, 3, 4, 5])
print(s)
s.replace(1, 5)
print(s)
