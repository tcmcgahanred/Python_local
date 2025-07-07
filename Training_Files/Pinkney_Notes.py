#################################################################################
#FILE NAME: test.py
#AUTHOR: I.Pinkney
#CREATION DATE: 30-Sep-2019
#LAST MODIFIED:
#DESCRIPTION:
#################################################################################
from random import randint
import string, collections
#import file #must be a python file
#from file import function

MAX = 100
MIN = 0
KING = "David"

def main():
    #output manipulation
    print (MAX)
    print ("Hello World")
    print ("hello", "world", sep=":", end="stupid head")
    #sep separates strings by a specific character.
    #end determines if output ends with a specific string certain string or not

    #integers and floats
    z = 3.45
    print (z == 3.14)
    print (z + 40)

    #string to integer and integer to string casting
    x = "80"
    y = 80
    print (int(x))
    print (str(y))

    #lists and tuples
    name = 'Pinkney'
    ''.join(reversed(name)) #join puts a list of elements together by a certain character
    a = [1, 2, 3, 4, 5]
    print (a)
    print (a[-1]) #-1 accesses the last element of a list
    s = "Give me words"
    print (list(s)) 
    l = ([1, 2], [3, 4]) #tuples are immutable
    print(type(l))
    l[0][0] = 9
    print(l)
    #list functions
    d = [1, 2, 3, 4, 5]
    sq = []
    for item in d:
        sq.append(item**2) #append adds an element to the end of a list
    print(sq)
    print (d[:3]) #colons operate in a [start:stop:step] format
    print (d[::2])
    print (d[1::2])
    print (d[::-1])

    #splitting and joining and formatting
    b = "string that i am using for this class" 
    message = b.split() #split divides a string into a list based off a certain character. Default is ''
    message[0] = "trash"
    myvar = "".join(message)
    print ("This is the test {}".format(b)) #format inserts a value into the area of a string with {}
    print ("Infinity is not {:.3f}. It is FOREVER!".format(23452.334465576868768)) #.3 means only display the 3rd number in the decimal, f means float 
    print (message)
    print (myvar)
    email = "hacker@stupidhead.com"
    email_split = email.split('@')
    email_join = '.'.join(email)
    print (email_join)

    #slicing
    print (b[:-1])
    print (message[:-1])
    
    #range
    print(range(10))#range operates in (start, stop, step) like the colons in a list
    for i in range(3, 30, 3):
        print(i)
        
    #challenge with split, join & replace
    email = 'jason@codehugger.com'
    print('.'.join(email.split('@')).split('.')[:-1])
    print(email.replace('@', '.').split('.'))#replace replaces an character in a string with another

    #input
    name = input("What\'s your name?")

    #conditionals
    if 1 == 0: #if is what will execute if something is true
        print("my bush is bigger")
    elif 1 < 0: #elif is the alternative if the if isn't true
        print("no it\'s not")
    else: #else if the default if nothing else is true
        print("both of y\'all stupid")

    #while loops: Remember DRY: Don't Repeat Yourself
    counter = 0 #while loops need something to change to stop running, or they will run forever
    while True: #while loops are used to repeat a process over and over without writing it over and over
        counter += 1 #while loops are usually for when you don't how long it will be before you stop repeating
        print(str(counter))
        if counter >= 10:
            break #break will make a process stop
    
    #for loops
    string = "FOR THE KING!" #for loop are used to repeat a process too! (usually when you know when you're supposed to stop)
    for ch in string:
        print(ch)

    #ASCII
    print(ord('a'))             #prints the character in number form
    print(chr(97))              #prints the number in character form  
    print(bin(ord('a')))        #prints the character as a number, and converts the number to binary
    print(format(1, '0>8b'))    #formats the number into binary

    #files
    '''fp = open('test.txt', 'w+') #opens a file
    fp.read(10) #reads the first 10 characters of a file
    fp.close()  #closes a file
    fp.closed   #checks to see if a file is closed
    fp.readlines() #reads all the lines of a file
    fp.readline()  #reads one line of a file
    
    with open('test.txt', 'w') as fp: #will keep file closed after execution is done
        for line in fp.readlines():
            print(line, end='')
    #r = read, w = write, a = append
    with open('test.txt', 'a') as fp:
        fp.writelines(["Soon ", "You ", "Be ", "DEAD"])'''

    #sets: set() is used to make an empty set
    s = {1, 2, 3, 4, 5} #sets do NOT maintain order and do not have duplicates
    print(s)
    l = [1, 1, 2, 2, 2, 63] 
    print(set(l))
    print(s.union(l))           #puts all the elements of 2 sets s & l together into a new set
    print(s.difference(l))      #finds all elements in the s set that are also not in l
    print(s.intersection(l))    #finds all the elements in s that are also in l
    s.add(6)                    #adds 1 new element to the set
    print(s)
    s.update({30, 50, 29})      #adds a sequence of new elements to a set
    print(s)

    #dictionaries: {} is an empty dictionary!!!!!
    d = {
        'key' : 'value',    #dictionaries use keys to access values in the dictionary
        'thing': 'meaning'
        }
    print(d['key'])         #the name of the dictionary key is used as the index
    d['key'] = 35
    d['fruit'] = True       #if the key doesn't exist but you set it to a value, it will be added to the dictionary
    print(d)                #if the key doesn't exist and you don't set it, it will not work!
    print(sorted(d.items(), reverse = True)) #sorted will sort the items. reverse puts them in reverse order

    for item in d: #item is the key
        print(item)
        print(d.items()) #prints key and it's value

    for item in d.values(): #item is the value
        print(item)

    s = 'the quick brown fox jumps over the lazy dog!!!'
    d = {}
    for c in s:
        d[c] = d.get(c,0) + 1
        '''if c in d:
            d[c] += 1
        else:
            d[c] = 1'''
    d.get(1, 'default')
    print(d)
    print(s.count('t'))

    for k, v in d.items():
        print(k, v)

    l = ['a', 'z', 'b', 'd', 'c']
    print(''.join(sorted(set(s))))
    print(sorted(set(s), key=len)) 
    print(max(l))       #max finds the maximum value
    print(min(l))       #min finds the minimum value
    print(max(sorted(l), key=len))
    print(min(sorted(l), key=len))
    print(collections.Counter(s))
    print('{} {} for {} miles.'.format(*l))

    #in python all chars are unicode
    print(0b10000)#binary
    print(0x10)   #hex
    print(0o20)   #octal
    print(bin(16))
    print(hex(16))
    print(oct(16))
    print(int('0b10000', 2))
    print(int('0x10', 16))
    print(int('0o20', 8))

    b = b'hello\x80'
    print(b[0])
    print(chr(104))
    print(ord('h'))

    #bytes are immutable.
    bytes('hello', encoding='ascii') 
    bytes('hello', encoding='utf-8')
    bytes('hello\x80', encoding='utf-8') #chars above 127 require multiple bytes to encode

    #bytearrays are mutable
    b = bytearray(b'hello')
    b.append(104)
    print(b)
    del b[-1]
    print(b)

    #bitwise operators. USE TRUTH TABLES!!!!
    #&  #AND
    #|  #OR
    #^  #XOR
    #~  #NOT
    #<< #left shift: moves all the digits over to the left
    #>> #right shift: moves all digits over to the right
    print(1 & 1) #prints as a decimal number 
    print(0 | 0)
    print(0b1001 & 0b0001)#prints as a decimal number
    print(bin(0b1001 & 0b0001)) #determines if each bit(0 or 1) of each number combined is true(1) or false(0).
    #the combination of each result is a new binary number that can be converted to hex, decimal, octal, etc.
    print(bin(0b11111111 & 0b111111100)) #prints as a binary number (byte) with 0b in front
    print(format(0b11111111 & 0b0111111, '0>8b')) #prints as binary number (byte)
    print(1 << 7)
    print(0b100 << 2)
    print(4 >> 1)
    print(4 >> 7)
    print(0b100 >> 2)
    #josephus problem
    bin(((41 << 1) & 0b11111111) | 0b1)
    #|= sets a bit. & (with whatever they gave you) checks a bit (0 = not set, 1 = set)

    n = 0
    x = 105
    ret = 0

    if n == 0 or n == 1:
        ret |= 0x10
    if x > 100:
        ret |= 0x20
    print(ret)

    n = 0
    x = 105
    ret = 0
    
    if n != 0 and n != 1:
        ret |= 0x10
    if x > 100:
        ret |= 0x20
    print(ret)
    
    '''d = {}
    with open('/etc/resolv.conf') as fp:
        for line in fp:
            ls = line.split()
            d[ls[0]] = ls[1]'''

'''functions
def rename_usacys():
    with open('C:/Users/isaac/AppData/Local/Programs/Python/Python37-32') as infile, open('passwd.txt', 'w') as outfile:
        for line in infile:
            fields = line.split(':')
            if fields[0] == 'usacys':
                fields[0] = 'usacys2'
                outfile.write(':'.join(fields))

def foo(a, b, c=1):
    return a+b+c
foo(1,2)
foo(1, 2, 3)
foo(c = 1, b = 2, a = 3)
d = {'a':1, 'b':2, 'c':3}
foo(**d)
def foo(*args) #any number of params
def foo(**kwargs) #wraps up any number of keyword arguments in a dictionary

def foo(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
foo(1, 1, a = 1, b = 2, c = 3)

y = lambda x: x + 100
y(1)'''

if __name__ == "__main__":
    main()
    #rename_usacys()
