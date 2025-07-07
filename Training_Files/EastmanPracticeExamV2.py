#!/usr/bin/env python3
import re
import statistics

def q1(floatstr):
    '''
    TLO: 112-SCRPY002, LSA 3,4
    Given the floatstr, which is a comma separated string of
    floats, return a list with each of the floats in the 
    argument as elements in the list.
    '''
    return list(map(lambda x: float(x), floatstr.split(',')))
    pass

def q2(*args):
    '''
    TLO: 112-SCRPY006, LSA 3
    TLO: 112-SCRPY007, LSA 4
    Given the variable length argument list, return the average
    of all the arguments as a float
    '''
    return statistics.mean(args)
    pass

def q3(lst,n):
    '''
    TLO: 112-SCRPY004, LSA 3
    Given a list (lst) and a number of items (n), return a new 
    list containing the last n entries in lst.
    '''
    return lst[len(lst)-n:]
    pass
    
def q4(strng):
    '''
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY006, LSA 3
    Given an input string, return a list containing the ordinal numbers of 
    each character in the string in the order found in the input string.
    '''
    return list(map(lambda x: ord(x), list(strng)))
    pass

def q5(strng):
    '''
    TLO: 112-SCRPY002, LSA 1,3
    TLO: 112-SCRPY004, LSA 2
    Given an input string, return a tuple with each element in the tuple
    containing a single word from the input string in order.
    '''
    return tuple(strng.split())
    pass

def q6():
    '''
    TLO: 112-SCRPY006, LSA 4
    Given an input string similar to the below, craft a regular expression  
    pattern to match and extract the date, time, and temperature in groups  
    and return this pattern. Samples given below.
    Date: 12/31/1999 Time: 11:59 p.m. Temperature: 44 F
    Date: 01/01/2000 Time: 12:01 a.m. Temperature: 5.2 C
    '''
    return 'Date:\s+(\d{1,2}/\d{1,2}/\d{4})\s+Time:\s+(\d{1,2}:\d{2}\s+[AaPp]\.[Mm]\.)\s+Temperature:\s+(\d+\.{0,1}\d*\s+[FfCc])'
    pass

def q7(filename):
    '''
    TLO: 112-SCRPY005, LSA 1
    Given a filename, open the file and return the length of the first line 
    in the file excluding the line terminator.
    '''
    return len(open(filename,'r').readline().strip('\n'))
    pass

def q8(filename,lst):
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY005, LSA 1
    Given a filename and a list, write each entry from the list to the file
    on separate lines until a case-insensitive entry of "stop" is found in 
    the list. If "stop" is not found in the list, write the entire list to 
    the file on separate lines.
    '''
    open(filename,'w').write(re.split('stop\n','\n'.join(lst),flags=re.I)[0])
    pass

def q9(miltime):
    '''
    TLO: 112-SCRPY003, LSA 1
    Given the military time in the argument miltime, return a string 
    containing the greeting of the day.
    0300-1159 "Good Morning"
    1200-1559 "Good Afternoon"
    1600-2059 "Good Evening"
    2100-0259 "Good Night"
    '''
    return (lambda time: "Good Night" if time >= 2100 or time < 300 else ("Good Morning" if time <=1159 else ("Good Afternoon" if time <=1559 else "Good Evening")))(miltime)
    pass
    
def q10(numlist):
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1
    Given the argument numlist as a list of numbers, return True if all 
    numbers in the list are NOT negative. If any numbers in the list are
    negative, return False.
    '''
    return (min(numlist)>=0)
    pass

