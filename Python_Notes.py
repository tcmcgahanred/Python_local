#endianess 
#byte encoding decoding
#struct

#COMMANDMENTS

# check your data!!!!!! use type() on everything you're ingesting first to confirm it hasn't changed!!!!!!!!!

# import sys
# print(sys.path)
# Add path sys.path.append(r'C:/directory/of/choice/') # note the 'r' at the start. Turns string into raw string, which Windows will accept.
# sys.path.remove('path')
# import importlib
# use reload() to reload a module to make use of a new/changed function with importlib.reload(modulename)
# import pathlib
# pathlib.Path.cwd() or pathlib.Path.home()
# "pip install python-registry"
# from Registry.Registry import Registry
# import requests
# from collections import Counter


########################################################################################################################

###ID / TYPE ###

# x = 15
# id(x) #this would give me an memory ID for x#
# type(x) # will tell me what type of object 'x' is, such as a string#

###APPEND###

# a = [1,2,3,4,5,6]
# a.append(7)
# print(a) #prints 1 thru 7#

###LIST###

# dog = 'dog'
# print(list(dog)) #prints ['d', 'o', 'g'] #

# x = list(('apple', 'banana', 'cherry'))
# print(x) #prints ['apple', 'banana', 'cherry'] #

# print(list(range(5))) #prints [0, 1, 2, 3, 4]
# print(list(range(0,5))) #prints [0, 1, 2, 3, 4]

# x = list(range(0,10,1))
# x[3] = 'k'
# print(x) #prints [0, 1, 2, 'k', 4, 5, 6, 7, 8, 9] # note that 'k' replaced 3.

# list1 = ['1', '2', '3']
# str1 = ' '.join(list1)
# print(str1) #prints '1 2 3'. Note that they're spaced out b/c there's a space in ' '.join() # #convert list to string #

###TUPLES###

#DON'T CREATE A BLANK TUPLE#

# tuples are immutable# f/home/usacys/Desktop/Rando.pyormat #
# t = (1,2,3,4,5) #tuples are designated with ()#
# can't change this with something like t[0] = 9 #

# def into(name, gender,age,bday_month,hometown):
#     return (name, gender,age,bday_month,hometown) #This returns the data as a tuple #

###SETS###

# s = {1,4,3,2,5,4} #there really isn't an order to a set# CANNOT index within a set, meaning, I can't use s[0]#
# print(s) #this'll print the set, without the duplicates, but, will not sort or order them#
# #use set(l) #to change list to a set#

# setl = {1, 4, 3, 2, 5, 4}  # there really isn't an order to a set# CANNOT index within a set, meaning, I can't use s[0] #
# setl.update([4, 5, 2, 3, 4, 1])
# setl.add(6)
# print(setl)
# print(setl)  # this'll print the set, without the duplicates, but, will not sort or order them#
# setToList = [1, 2, 3, 4, 5, 6]
# print(set(setToList))  # to change list to a set#

#LIST and SETS#

# s = {1,4,3,2,5,4,9,9,1,4,6}
# print(sorted(list(set(s)))) #prints [1, 2, 3, 4, 5, 6, 9] #note that it removed duplicates from the set(to the list) #

###DICTIONARY###

#update() a dictionary #

# d = {'key0':'value0','key1':'value1'}
# print(d)/home/usacys/Desktop/Rando.py
# #a = {} #Note that this can be mistaken for an empty set, but to make an empty set, you have to use set() instead#
# d['key0'] = 'somethingelse' # to change the value of key0#
# d['key3'] = 'new item'

# iterating over a dictionary with FOR#
# d = {'key0':'value0','key1':'value1'}

# for item in d:
#     print(item) #this'd print out the keys#

# for item in d:
#     print(d[item])  #prints the values belonging to keys#


# adding contents from linux DNS file to a dictionary. Contains URLs and email addresses#
# d = []
# with open('/etc/resolv.conf') as fp:
#     for line in fp:
#         ls = line.split()
#         d[ls[0]] = ls[1]

# You don't have to add the colon between the key and value yourself, b/c python knows to add it natively#

# create a dictionary from a random string. Counts occurrence of every element, including spaces#

# s = 'the quick brown fox jumps!!!'
# d = {}
# for c in s:
#     if c in d:
#         d[c] += 1
#     else:
#         d[c] = 1
# print(d) #prints {'t': 1, 'h': 1, 'e': 1, ' ': 4, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 1, 'o': 2, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, '!': 3}
# print(s.count('o')) #prints 2 #

# # for default keys values
# s = 'the quick brown fox jumps!!!'
# d = {'t': 1, 'h': 1, 'e': 1, ' ': 4, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 1, 'o': 2, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, '!': 3}
# d['t'] = 1
# print(d['t']) #prints a 1 b/c there's only 1 't' #
# for c in s:
#     d[c] = d.get(c,0) + 1 #EXAM# #count occurrence of a string #
# print(d)
#
# #DICT### Sum of all the key values#
#
# d = {'t': 1, 'h': 1, 'e': 1, ' ': 4, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 1, 'o': 2, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, '!': 3}
# x = sum(d.values())
# print(x) #prints 28#

# sally = 'sally sells sea shells by the sea shore and by the road'
# characters = {}
# for char in sally:
#     if char in characters:
#         characters[char] += 1
#     else:
#         characters[char] = 1
# print(characters) #prints {'s': 8, 'a': 5, 'l': 6, 'y': 3, ' ': 11, 'e': 7, 'h': 4, 'b': 2, 't': 2, 'o': 2, 'r': 2, 'n': 1, 'd': 2}

# #find the min value and its key#
# characters = {'t': 1, 'h': 2, 'e': 3, ' ': 4}
# k,n = characters.items()[0]
# for key,v in characters.items():
#     if v < n:
#         k = key
#         n = v
# print(characters) #WON'T THIS WORK, because it's not python 3.7.3#

# def number(n):
#     d = {0:'zero', 1:'one',2:'two', 3:'three',4:'four'}
#     return d[n]
#
# for i in range(0,5):
#     print(number(i)) #prints out dictionary values iteratively#

# gold = {'usa':31,'UK':19}
# num_medals = []
# for ky,vl in gold.items():
#     num_medals.append(vl) #you could change the arg to either the key or the value and it'd be sent to the blank list #
# print(num_medals) #prints [31, 19], which prints just the values of the dictionary #

###FORMAT###

# a = input('What\'s your name?') #enter 'Tim' #
# b = input('What are you doing today?') #enter 'going to church' #
# print('Hello,{}. Have fun {} today.'.format(a, b))
#
# print('PI = {:.10f}'.format(3.141592653598)) #prints 'PI = 3.1415926536'. If changed to .01f, it'd only be '3.14' #
# print('thousands comma = {:,}'.format(1234567890)) # :, adds a thousandth place separator comma #
#
# inventory = ['dog, cat, bird']
# for item in inventory:
#     fields = item.split(', ') #split of inventory by item and use those contents to fill in the string #
#     print('The store has {} {}, each for {} USD.'.format(fields[1], fields[0], fields[2])) #prints The store has cat dog, each for bird USD. #

#x = format(0.5, '%')
#print(x) #prints 50.000000%

###SPLIT### a string into a list #

# txt = 'welcome, to the, jungle'
# x = txt.split()
# print(x) #prints a list ['welcome', 'to', 'the', 'jungle'] #
# print(txt.split()) #splits each word up into a list #
# print(txt.split(', ')) #prints  ['welcome', 'to the', 'jungle'] #Split up by the commas #
# print(txt.split('the, ')) #prints  ['welcome', 'to the', 'jungle'] #Split up by the commas #
# print(txt[:-1]) # removes the 'e' off the end because it's a string and not a list.#

# email = 'timbo@gmail.com'
# var1 = email.split('@')
# print(var1) #['timbo', 'gmail.com']
# var2 = '.'.join(var1) #this joins the two list elements on the '.' #
# print(var2) #prints timbo.gmail.com
# var3 = var2.split('.')
# print(var3) #prints ['timbo', 'gmail', 'com']

# something = 'hello'
# print(list(something)) #prints o['h', 'e', 'l', 'l', 'o'] # string to list #
# print(''.join(something))    #prints 'hello' # list to string #

# print('hello', 'world', sep=':') #prints hello:world #
# print('hello', 'world', sep=':', end='0') #removes the break to the next line #
# print('hello', 'world', sep=':', end='\n\n\n') #adds 3 new lines at the end #

# L = [0.34, '6', 'SI106', 'Python', -2]
# print(len(L[1:-2])) #prints 2, the length of the split #

# singers = 'Peter, Paul, and Mary'
# print(singers[0:5]) #prints 'Peter' #
# print(singers[7:11]) #prints 'Paul' #
# print(singers[17:21]) #prints 'Mary' #
#
# fruit = 'banana'
# print(fruit[:3]) #prints 'ban' #
# print(fruit[3:]) #prints 'ana' #
# print(fruit[:]) #prints 'banana' #
#
# julia = ('Julia', 'Roberts', 1967, 'Duplicity', 2009, 'Actress', 'Atlanta, Georgia') #split up and join a tuple #
# julia = julia[:3] + ('Eat Pray Love', 2010) + julia[5:]
# print(julia) #prints out ('Julia', 'Roberts', 1967, 'Eat Pray Love', 2010, 'Actress', 'Atlanta, Georgia')

###REPLACE###
#EXAM#

# email = 'timbo@gmail.com'
# email_split = email.split('@')
# print(email.replace('@', '.').split('.')[:]) #prints ['timbo', 'gmail', 'com']
# print(email.replace('@', '.').split('.')[:-1]) #prints ['timbo', 'gmail']
# print(email.replace('@', '.').split('.')[:1]) #prints ['timbo']

# words = 'This is a rock'
# print(words.replace(' ', '')) #prints 'Thisisarock' # replaced a space with no space #

# def song_decoder(song):
# return ' '.join(song.replace('WUB', ' ').split())

###JOIN###

# words = 'This is a rock' #This won't work b/c it's a string. Need to make it a list#
# print(''.join(words))
# words = ['This', 'is', 'a', 'rock'] #
# print(''.join(words)) #prints Thisisarock' #list to string #
#
# words = ('John', 'Peter', 'Vicky')
# print(''.join(words)) #prints 'JohnPeterVicky' #tuple to string #

# myDict = {'name': 'John', 'country': 'Norway'} #dictionary join #
# mySeparator = 'TEST'
# print(mySeparator.join(myDict)) #prints 'nameTESTcountry' #defaults to printing the key, not the value #
# print(mySeparator.join(myDict.values())) #prints 'JohnTESTNorway', which is the values #

# myTuple = ('John', 'Peter', 'Vicky')
# x = ''.join(myTuple)
# print(x) #prints 'JohnPeterVicky' #

# wds = ['red', 'blue', 'green']
# glue = ';'
# s = glue.join(wds)
# print(s) # prints 'red;blue;green' #
# print(wds) #prints ['red', 'blue', 'green'] #
# print('***'.join(wds)) #prints 'red***blue***green' #
# print(''.join(wds)) #prints 'redbluegreen'

# wrds = ['happen', 'occurr']
# for i in range(len(wrds)):
#     wrds[i] =wrds[i] + 'ed'
# print(wrds) #prints ['happened', 'occurred'] #past tense versions #

###ZIP###

# b = {'key0':'value0','key1':'value1'}
# c = {'key2':'value2','key3':'value3'}
# x = zip(b.values(), c.values())
# print(list(tuple(x)))

###RANGE###

# r = range(0,9)
# print(list(r)) #prints [0, 1, 2, 3, 4, 5, 6, 7, 8] #
#
# #
# for x in range(3):
#     print('This line will execute three times') #prints 'This line will execute three times' three times
#
# x = range(6)
# for n in x:
#   print(n) #prints 0 to 5 iteratively#
#
# for x in range(0,25,5):
#     print(x) #prints iteration of 5, 10, 15, 20 #
#
# l = [1,2,3,4,5,6,7,8,9,10]
# print(l[1:10:2]) #prints [2, 4, 6, 8, 10] #

# print(list(range(5))) #prints [0, 1, 2, 3, 4] # convert range to list# #
# print(list(range(0,3))) #prints [0, 1, 2] # convert range to list#

# print([i**2 for i in range(1,11) if i%2 == 0]) #prints [4, 16, 36, 64, 100]
# print([1 for n in range(10)]) #prints [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# r = range(0,9)
# i = iter(r)
# print(next(i)) #prints '0' #

###LEN###

#note that blank spaces count as characters#

# fruit = 'grape'
# midchar = [len(fruit)/2]  #access middle character of a string by using /2, which is 'a'
# print(midchar) #prints '2.5' #

# alist =  ['hello', 2.0, 5]
# print(len(alist)) #prints 3, the length of the list #
# print(len(alist[0])) #prints 5, the length of the element in the 0 position, 'hello' #

###SWAP###

#clever way to swap first and last element. This works because it's a list already#
# a = [1,2,3,4,5]
# a[0], a[-1] = a[-1], a[0]
# print(a) #prints [5, 2, 3, 4, 1]
#
# a = 'hello world'
# b = list(a) # string to list #
# b[0], b[-1] = b[-1], b[0]
# print(b) #prints ['d', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'h'] #
# print(''.join(b)) #prints 'dello worlh' #list to string #

###SORT###
#The sort() method sorts the list ascending by default.

# l = [5,3,2,1,4]
# l.sort()
# print(l) #prints [1, 2, 3, 4, 5]
# l.sort(reverse=True)
# print(l) #prints [5, 4, 3, 2, 1] #

# def myFunc(e):
#   return len(e)
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
# cars.sort(key=myFunc)
# print(cars) #prints ['VW', 'BMW', 'Ford', 'Mitsubishi'], the list from shortest to longest #

###SORTED###
#The sorted() function returns a sorted list of the specified iterable object
#Note that sorted() can specify ascending or descending # sorted(a, reverse=True) #

# a = ("h", "b", "a", "c", "f", "d", "e", "g")
# print(sorted(a)) #prints ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] #

##find the average of the given data excluding the highest and lowest#
# scores = [90.3,47.7,85.0,100.0,50.1,0.0]
# scores2 = [91.3,57.7,81.0,100.0,55.1,0.0]
# def avg_without_outliers(data):
#     sscores = sorted(data)
#     sscores = sscores[1:-1] #removes outliers, e.g. 0.0 and 100.0 #
#     return sum(sscores)/len(sscores) #average #
# print(avg_without_outliers(scores)) #prints 68.275 #calling the function and passing in the variable scores #
# print(avg_without_outliers(scores2)) #prints 71.275 #calling the function and passing in the variable scores2 #
# print(avg_without_outliers([1,2,3,4])) #prints 2.5 #calling the function and passing in the values 1,2,3,4 #

###SORTED DICTIONARY###

# t = {'a':0, 'b':1, 'c':2}
# print(sorted(t)) # prints ['a', 'b', 'c'] #dictionary to list # by default, prints the keys, not the values #
# print(sorted(t, reverse=True)) #reverse#  prints ['c', 'b', 'a']
# print(sorted(t.values(), reverse=True)) # prints [2, 1, 0]
# print(sorted(t.items(), reverse=True)) # prints[('c', 2), ('b', 1), ('a', 0)]

# def keyfunc(t):
#     return t[1]
#
# print(sorted(t.items(), key=keyfunc)) # prints[('a', 0), ('b', 1), ('c', 2)]

# l = ['abc', 'zz', 'bcde', 'a', 'defghi']
# print(sorted(l)) #prints ['a', 'abc', 'bcde', 'defghi', 'zz'] #
# print(sorted(l ,key=len)) # prints ['a', 'zz', 'abc', 'bcde', 'defghi']
# print(len(sorted(l,key=len)[-1])) #prints 6, the length of 'defghi', using the list ['a', 'zz', 'abc', 'bcde', 'defghi'] #key length #
# print(max(l)) #prints zz b/c, alphabetically, it's the highest in the list#
# print(max(l, key=len)) #prints 'defghi' because it's the longest in the list #

###SLICE###
#first argument is inclusive and second is exclusive #

# sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
# print(sports[-3:]) #prints ['curling', 'ping pong', 'hockey'] # started at the 3rd from the end #
# print(sports[3:]) #prints ['baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey'] # starting at the 4th position (0,1,2,3) #

###INDEX###

# awards = ['Emmy', 'Tony', 'Academy', 'Grammy']
# pos = awards.index('Tony')
# print(pos) #this'll give a 1 b/c it's in the 1 place. (e.g. 0, 1)#

###COUNT###

# rv = 'Once upon a midnight dreary,...'
# print(int(rv.count(''))) #prints 32, which is the number of elements in the string. Change the argument if needed.#

#or use FOR and IF to count through a list#

# s = 'We are learning!'
# x = 0
# for i in s:
#     if i in ['a', 'b', 'c', 'd', 'e']:
#         x += 1
# print(x) #prints out a 5 b/c we c ount 5 of those letters in the s string #

###ITER###

# x = iter(['apple', 'banana', 'cherry'])
# print(next(x)) #prints 'apple' #
# print(next(x)) #prints 'banana' #
# print(next(x)) #prints 'cherry' #

###REVERSED###

# p_phrase = 'was it a car or a cat I saw'
# r_phrase = ''.join(reversed(p_phrase)) #becomes a list with reversed and then it's joined back into a string #
# print(r_phrase) #prints 'was I tac a ro rac a ti saw'

#or#

# r_phrase = p_phrase[::-1] #method 2 without using reversed()#
# print(r_phrase) #prints 'was I tac a ro rac a ti saw'

#or#

# alph = ['a', 'b', 'c', 'd']
# ralph = reversed(alph)
# for x in ralph:
#   print(x) #prints the list iterively and reversed #

#or#

# return ' '.join(reversed(sentence.split())) #EXAM# be aware of the need for a space as a join argument #

###LAMBDA###

# anon function that we don't give a name to#

# y = lambda x: x + 100 #a function you only use once#
# print(y(1)) #prints 101

# l =[(9,5), (5,3), (6,9)]
# print(sorted(l,key= lambda t: t[1]))

###chr()###

# Get the character that represents the unicode 97:
# x = chr(97) #97-122 is the alphabet#
# print(x)   #prints an 'a'

###ORD###

# The ord() function returns the number representing the unicode code of a specified character.#
# print(ord('a')) #prints 97


###TRANSLATE###

# t = { ord('a'): 'zzz', ord('g'): None }
# s = 'abcdefg'
# print(s.translate(t))  #prints 'zzzbcdef'

# t = { ord('1'): 'aaa', ord('b'): 'bbb', ord('c'): 'ccc', ord('d'): 'ddd', ord('e'): 'eee', ord('f'): 'fff' }
# s = 'abcdef'
# print(s.translate(t))  #prints 'zzzbcdef'

###maketrans()###

# print(str.maketrans('abcdefghijklmnopqrstuvwxyz','bcdefghijklmnopqrstuvwxyza'))

###DEQUE###
#
# from collections import deque
#
# d = deque('abcdefg')
# print(d)
# d.rotate(1)
# print(d)

###DIR###

# run in python CLI
# import random# #pull in the random module
# dir() allows you to
# from random import randint, \
#     choice  # now, if I create a list, i can print random elements from that list by using choice(listName)
# from random import *  # pulls in everything from the module into name space, allowing access to all random functions#

# mymodule.utility('something')

###UNPACKING####
#refers to the use of *2 or *3

# s = 'Nick, lowcrawled, 27'
# s2 = s.split(', ')
# print(s2)
# print('{} {} for {} miles.'.format(s2[0],s2[1],s2[2])) #prints 'Nick lowcrawled for 27 miles.'
# print('{} {} for {} miles.'.format(*s2)) #This is called unpacking#
# s3 = ['Nick', 'lowcrawled', '27', 'additional']
# print('{} {} for {} miles.'.format(*s3)) #This is called unpacking#

###variable length position argument and variable length key argument###

# def foo(a,b,c):
#    return a+b+c
#
# print(foo(c=3, b=2, a=1))
# def foo(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
# print(foo())
# print(foo(1,1,a=1,b=2,c=3))

###FILES###
#DO NOT PUT QUOTES AROUND FILENAME #


# d = []
# with open(file_name) as fp: #as means you're assigning the file a name (fp), sorta..... #
#     for line in fp:
#         len()
#
# with open(filename) as fp:
#     return len(fp.readlines()[0].strip())

# with open('plain.pgm', 'rb') as fp:
#     data = fp.read()
# type(data)

# byte = 217
# print(bin(byte)) #prints 0b11011001'
# for i in range(7, -1, -1):
#     print((byte >> i) & 1) #prints the bytes '11011001' out iterively #

#if  bit 0x8 is on in n, set bit 0x80 in the return value #EXAM#
#if x > 100, set bit 0x10 in the return value #EXAM#
# def validate(n,x):
#     ret= 0
#     if (n & 0x8) == 0x8:
#         ret |=0x80
#     if x > 100:
#       ret |= 0x80
#
#     return ret

#to write a new line to a file #
#fp.write(item+'\n')

#EXAM#
#     with open(filename, 'w') as fp:
#         for entry in lst:
#             if entry.lower() == 'stop':
#                 break
#             fp.write(entry+'\n')

#write one file to another #

# def question(infile):
#     with open(infile) as fp:
#         for line in fp:
#             print(line,end='') #cat, user_input, ispangram,text.txt
#
#     with open('infile', 'r') as source, open('outfile', 'w') as destination:
#         destination.write(source.read())

###BIT manipulation###

# a = 42
# print(bin(a))
# print(format(a, '#b'))

'''The '#' option causes the “alternate form” to be used for the conversion.
The alternate form is defined differently for different types.
This option is only valid for integer, float, complex and Decimal types.
For integers, when binary, octal, or hexadecimal output is used, this option
adds the prefix respective '0b', '0o', or '0x' to the output value. For floats,
complex and Decimal the alternate form causes the result of the conversion to always
contain a decimal-point character, even if no digits follow it. Normally, a decimal-point character
appears in the result of these conversions only if a digit follows it. In addition, for 'g' and 'G'
conversions, trailing zeros are not removed from the result.'''

# print(format(a, 'b')) #format type 'b' for 'Binary format. Outputs the number in base 2.'#
# print(format(a, '0>8b')) #converted to a binary string, zero-filled, right aligned, width of 8.#

###int() arguments for dealing with binary literal###

# print(0b11) #prints a 3 as an integer#
# print(type(0b11))
# print(int(0b11)) #prints a 3#
# print('0b11') #prints out '0b11' as a string#
# #print(int('0b11')) #throws an error#
# print(int('0b11',2)) #the 2nd argument fixes the above issue ^#

###Working with bytes###

# b = b'hello'
# b.insert(o,104)
# b = bytearray(b'hhello')
# b = b.insert(0,104)
# print(b) #prints  bytearray(b'hhello')
# bin(ob1001 & 0b0001)
# #prints '0b1'
# 0b0001
# #prints 1

#format(0b11111111 & 0b01111111, '0>8b')
#prints 0b1111111 #

###bit check###
'''by anding the value with a mask consisting of a 1 in the position of the bit you wish to check. 
If the result of the operation is equal to the mask, then that bit was set'''

#bin(0b101010101 & 0b00000010)
#prints '0b10'


# if 250 & 1 == 1:
#     print('LSB is set')
# if 251 & 1 == 1:
#     print('LSB is set')

#bitwise operators https://www.w3schools.com/python/python_operators.asp
# & | ^ ~ << >>
# & and # Sets each bit to 1 if both bits are 1
# | or # Sets each bit to 1 if one of two bits is 1
# ^ exclusive or # Sets each bit to 1 if only one of two bits is 1
# ~ not # Inverts all the bits
# << left shift # Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> right shift # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# print(0b111101110 & 0b00000001) #prints a 0 b/c it'd need to be 1 and 1 across each string to print a result #
# print(0b111101110) #prints 494 #
# print(0b111101110 | 0b00000001) #using the or operator #
# #prints 495 #note the one number difference #

#if n is a zero or a one, return an integer with bit 0x10 set #

# def validate(n, x):
#     if n == 0 or n == 1: #logical or operator #
#         return 0x10
#
# # if x > 100, set bit 0x20 in the return value #
#
# def validate(n, x): # #requires if statements, not elif or else # #EXAM#
#     ret = 0
#     if n == 0 or n == 1: # * example if !==0 and n !==1: #
#         ret |= 0x10
#     if x > 100:
#         ret |= 0x20
#
#     return ret

# * if the if statement is changed to use ! (not statements), use AND instead #EXAM #

###SHIFT operator###

# 1 << 1 # prints a 2
# 1 << 2 # prints a 4
# print(1 << 7) #prints a 128 #
#
# print(2 >> 1) #prints a 1 #
# print(128 >> 7) #prints a 1 #
# print(0b100 >> 2) #prints a 1#

#  00101100 #original
# 101100000 # << 3
#  00001011 # >> 2

# print(bin(41)) #prints '0b101001' #
# print(bin(41 << 1)) #prints '0b1010010', which is 82. It shifted all the bits to the left one position #
# print(bin((41 << 1) & 0b111111)) #print '0b10010' #
# print(bin(((41 << 1) & 0b111111) | 0b1)) #prints '0b10011' #
# print(0b10011) #prints a 19 #
# print(0b1010010)

###NOT operator###

# print(bin(251)) #prints 0b11111011
# print(bin(251 & ~1)) #prints 0b11111010 # note that the LSB switched #

#check to see if a paritcular bit is set #
# n = 15
# print(bin(n))   #prints 0b1111
# print((n & 0b1000) == 0b1000) #if True, then the bit was set #prints True

#if bit 0x8 is on in n, set bit 0x80 in the return  value #EXAM#
# def validate(n):
#     ret = 0
#     if (n & 0x8) ==0x8: #() so that you can easily identify the precendence of the operation #
#         ret |= 0x80
#
#     return ret

# print(0x8) #prints 8
# print(0x80)  #prints 128

#Attempt to <insert some operation here >. If the attempt succeeds, return True.Otherwise, return False: #EXAM#

# def test_question(filename): # don't add quotes #
#     try:
#         fp = open(filename)
#     except:
#         return False
#     return True

###Exception Handling###

# full_lst = ['ab', 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv']
#
# attempt = []
#
# for elem in full_lst:
#     try:
#         attempt.append(elem[1])
#     except:
#         attempt.append('Error')

###CLASS####

# class Name():
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def __printme(self):
#         print('{}, {}'.format(self.last,self.first))
#
# import i
# n = I.Name('Albert','Einstein')
# n = I.name('edsger', 'Djik')
#
#     def __str__(self):
#         return '{}, {}'.format(self.last, self.first)
#
# class Baloon():
#
#     def __init__(selfself, altitude):
#         self.altitude = 0
#
#     def rise(self):
#         self.altitude -= 1
#         if self.altitude < 0:
#             self.altitude = 0
#
#     def set_altitude(self, newaltitude):
#         self.altitude = newaltitude
#
#     def __str__(self):
#         return 'Baloon is at {} units altitude'.format(self.altitude)

#to use the baloon and make changes to 'altitude'
#import i
#b = i.Balloon(10)
#b.altitude would print 10 #
# b.rise() #b.altitude would print 11 #
# b.descend() #b.altitude would print 9 #
# b.set_altitude(5) #b.altitude would print 5 #
# str(b) #prints 'Baloon is at 5 units altitude'

###SOCKET###
#remember that var.connect() contains an enclosed tuple as a argument (e.g. var.connect((IP, PORT)) #

#import socket #import for library / to set up a server #
#
# def udp_echo_server(): #dont' forget the import and function call #
#     s = socket.socket(type=socket.SOCK_DGRAM) #DGRAM is UDP # socket is the name of the module and the .socket is the name of the object we're creating # (type=) defaults to IPv4 TCP #
#     s.bind(('',12345)) #could add IP addy within the quotes # designate the interface we want to connect to # argument is a tuple, whens the double (()) #
#     while True:
#         data,address = s.recvfrom(4096) #size per datagram (packet?)
#         print(data,'received from {}'.format(address))
#         s.sendto(data,address) #sending datagrams back to... #

# def udp_echo_client(): #dont' forget the import and function call #
#     s = socket.socket(type=socket.SOCK_DGRAM)
#     s.sendto(b'u haz ben ooned by timboslice' , ('192.168.242.99',12345))
#     data,address = s.recvfrom(4096)
#     print(data, 'echoed from {}'.format(address))

# def tcp_echo_server(): #dont' forget the import and function call #
#     s = socket.socket() #don't need to specify TCP, since it's the default #
#     s.bind(('',12345))
#     s.listen() #!!! one of the main differences between UDP and TCP for socket creation #
#
#     while True:
#         conn, address = s.accept()
#         print('connection accepted from {}'.format(address))
#
#         data = conn.recv(4096) #echo server needs to receive first and then send back #
#         print(data, 'received from {}'.format(address))
#
#         conn.sendall(data) #sendall() will send until done # Doesn't necessarily mean this'll work, since we're just asking to send. Can't force it, obviously #
#         conn.close()

# def tcp_echo_client(): #dont' forget the import and function call #
#     s = socket.socket() #TCP is the default argument #
#     s.connect(('192.168.242.99',12345)) #remember, the .connect() argument contains a tuple with the IP and port #
#     s.sendall(b'there are some who call me.... Tim')
#     echodata = s.recv(4096) #not gauranteed to work #
#     print(echodata, 'echoed from server')

# def qotd_client(): #quote of the day server # #dont' forget the import and function call #
#     s = socket.socket() #use default # / socket.setdefaulttimeout(5) /
#     s.connect(('djxmmx.net',17))
#     received = bytearray()
#     buf = s.recv(64) #if that came back with nothing, then it'd close #
#     while buf:
#         received.extend(buf)
#         buf = s.recv(64)

# echo protocol# TCP and UDP variants #
# RFC 862#
# socket.socket(#family IPv4 is AF_INET & type SOCK_DGRAM - UDP or SOCK_STREAM - TCP)
# echo server over UDP
# '''in order to use this:
# - go to CLI
# - navigate to python interpreter with 'python3'
# - import sockit #which is the name of the py file#
# - then use sockit.udp_echo_client()''' #this is the name of the function I want to use, either the client or server #
# For TCP, a server must be open. So, if you're using loopback, you must have your own server up. #
# Determine how much to read with: fixed length / length prefix framing / until read flag (e.g. 'sentinel') / RFC 865 'Quote of the Day Protocol' /

###BASE64###

# def b64dclient(connectto='192.168.242.99',port=12345): #parameters can be any IP/URL and port that we intend to pull data down from #
#
#     s = socket.socket() #use default #
#     s.connect((connectto,port)) #passed from function parameters #
#     payload = bytearray()
#     buf = s.recv(64)
#     while buf:
#         payload.extend(buf)
#         buf = s.recv(64)
#
#     # encoded = base64.encodebytes(b'hello\x80')
#     bcode = base64.decodebytes(payload)
#     cbcode = compile(bcode, '<string>', 'exec')
#     exec(cbcode)

# if __name__ == '__main__':
#     udp_echo_server()
#     udp_echo_client()
#     tcp_echo_server()
#     tcp_echo_client()
#     qotd_client()
#     qotd_client_try()
#     b64dclient()

##############FUNCTIONS#################################################################################################

###WHILE###
# Note the difference in this while loop
#
# a = 10
# while a > 0:
#     a -=1 #iterator is added here, before print
#     print(a) #this will print 10 to 1
#
# a = 10
# while a > 0:
#     print(a) # this will print 9 to 0
#     a -=1 #iterator is added here, after print

# l = [1,2,3,4,5]
# idx = 0
# while idx < len(l):
#     l[idx] = l[idx]**2
#     idx += 1
# print(l) #prints [1,4,9,16,25]# squares the element #

###FOR LOOP###

# l = [1,2,3,4,5]
# sq = []
# for item in l:
#     sq.append(item**2)
# print(sq) #prints nearly the same results as the aforementioned function; [1,4,9,16,25]#
# #if you indent the print, it'll produce a different result# iterate steps in multipules #

# words = ['adopt', 'bake', 'beam', 'confide', 'grill', 'plant', 'time', 'wave', 'wish']
# past_tense = []
# for word in words:
#    if word[-1] == 'e':
#        word = word + 'd'
#        past_tense.append(word)
#    else:
#        word = word + 'ed'
#        past_tense.append(word)
#
# print(past_tense) #['adopted', 'baked', 'beamed', 'confided', 'grilled', 'planted', 'timed', 'waved', 'wished'] #

# for x in 'banana':
#   print(x) #prints out the letters of 'banana'

# Basic accum #
# numbers = range(41)
# sum1 = 0
#
# for num in numbers:
#     sum1 = sum1 + num #
# print(sum1) #prints 820 #
#
# accum = 0
# for w in range(11): #or range(1,11) #
#     accum += w
# print(accum) #prints 55 #
# find words with 'w' #
# items = ['whirring', 'dog', 'ow']
#
# acc_num = []
# for item in items:
#     if 'w' in item:
#         acc_num.append(item)
# acc_num = len(acc_num)
## print(acc_num)
# str1 = 'I like nonsense'
# numbs = 0
# for i in str1:
#     numbs += 1
# print(numbs) #prints a 15#

# s1 = 'xyaabbbccccdefww'
# s2 = 'xxxxyyyyabklmopq'
# s3 = (s1 + s2)

# when placing something into an empty list, use append #
# new = []
# for unique in s3:
#     if unique not in new: #Great use of 'not in' #
#         new.append(unique)
# new.sort()
# print(''.join(new)) #prints 'abcdefklmopqwxy'

# guests = ['Tim', 'Donna', 'Amanda', 'Josie']
# for steps in range(4):
#     print(guests[steps]) #prints out each name iteratively #

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
# print(raise_to_power(2,2)) #prints 4. In print() need to add argument of (2,2) #

# def translate(phrase):
#     translation = ''
#     for letter in phrase:
#         if letter in 'AEIOUaeiou':
#             translation = translation + 'g'
#         else:
#             translation = translation + letter
#     return translation
# print(translate('hello fren')) #prints 'hgllg frgn' #

# num_lst = [3, 20, -1, 9, 10]
# is_even = []
# for num in num_lst:
#     if num%2 == 0:
#         is_even += ['True']
#     else:
#         is_even += ['False']
#
# print(is_even) #prints ['False', 'True', 'False', 'False', 'True'] #even number true or false #

###FOR LOOP average of list###

# s = sum(args) / len(args) #average simplified #

# week_temps_f = '75.1,77.7,83.2,82.5,81.0,79.5,85.7'
# temps=0
# count=0
# for temp in week_temps_f.split(','):
#    temps += float(temp)
#    count +=1
# avg_temp = temps / count
# print(avg_temp) #prints 80.67142857142858 #

#or

# scores = (s1 + s2 + s3) / 3 #average #
# if scores > 50:  # or if (s1+s2+s3)/3 > 50:
#     return 'GO'
# else:
#     return 'NOGO' #


# #find number of scores that are greater than or equal to 90 #
# scores = '67 80 90 97 78 88'
# a_scores = 0
# for score in scores.split():
#     if int(score) >= 90:
#         a_scores += 1
# print(a_scores) #prints a 2, b/c there's 2 scores that are >= 90 #

# #count words with the same first and last letter #
# sentence = 'some students are suspects'
# sentence_list = sentence.split()
# same_letter_count = 0
#
# for word in sentence_list:
#     if word[0] == word[-1]:
#         same_letter_count += 1
# print(same_letter_count ) #prints a 2 #

# find words with 'w' common letter #
# items = ['whirring', 'dog', 'ow']
#
# acc_num = []
# for item in items:
#     if 'w' in item:
#         acc_num.append(item)
# acc_num = len(acc_num)
# print(acc_num) #prints '2' #

# words with a certain length #

# words = ['water', 'chair', 'pen', 'basket', 'hi', 'car']
# num_words = 0
# for word in words:
#     if len(word) > 3:
#         num_words += 1
# print(num_words) #prints '3' #

###IF ELIF###

# if miltime > 300 and miltime < 1200:
#     return 'Good Morning'
# elif 1200 < miltime < 1600:
#     return 'Good Afternoon'
# elif 1600 < miltime < 2100:
#     return 'Good Evening'
# else:
#     return 'Good Night'

#or, can use 'if miltime in range(0300, 1200):' #need to make this 1200 though, not 1159, b/c the end time is 'non-inclusive' #

#FIZZBUZZ#

# n = input('Enter a positive number:')
#
# nums = [] #this section is to prevent explosion after bad input. Validate it# !!!!NEED TO KNOW THIS!!!!
# for ch in n:
#     if ch.isdigit():
#         nums.append(ch)
# n = int(''.join(nums))
#
# if n % 3 == 0 and n % 5 == 0:
#     print('Fizzbuzz')
# elif n % 3 == 0:
#     print('Fizz')
# elif n % 5 == 0:
#     print('Buzz')
# else:
#     print(n)



###Alternate instructor's version for one-liner purposes###

# i = int(input('Enter a positive number: '))
# print(not i%15 and 'fizzbuzz' or not i%3 and 'fizz' or not i%5 and 'buzz' or i)

###INVERT###
# invert pixels#

# things = [1,2,3,4,5,6]
# def inverted(things):
#     # cpy = 1[:]
#     # invert(cpy)
#     # return cpy
#     newl = []
#     for thing in things:
#         newl.append(str(255 - int(thing)))
#     return newl
# print(inverted(things))

###Object Functions###

# class student:
#
#     def __init__(self, name, major, gpa):
#         self.name = name
#         self.major = major
#         self.gpa = gpa
#
#     def on_honor_roll(self):
#         if self.gpa >= 3.5:
#             return True
#         else:
#             return False
#
# from student import student
# student1 = student('Oscar', 'Accounting', 3.1)
# student2 = student('Phyllis', 'Business', 3.8)
# print(student2.on_honor_roll())

###WHILE loop###

# wanswer = "0"
# while answer != "4":
#     answer = input("What is 2 + 2? ")
# print("Correct!") #will only print if input is '4'. #

# def sublist(numbers):
#     val = []
#     idx = 0
#     while idx < len(numbers):
#         if numbers [idx] == 5:
#             return val
#         val.append(numbers[idx])
#         idx += 1
#     return val

###OR do this with a for loop intstead###

# def sublist(numbers):
#     retval = []
#     for item in numbers:
#         if item == 5:
#             return retval
#         retval.append(item)
#         return retval

# def sublist (oldlist):
# newl = []
# for item in oldlist:
#     if item in oldlist:
#         if item != 'STOP':
#             break
#     newl.append(item)
# return newl

# idx = 0
#     while oldlist[idx] !_ 'STOP' and idx < len(oldlist):
#         idx += 1
#     return oldlist[:idx]

# byte = 217
# print(bin(byte)) #prints 0b11011001'
# for i in range(7, -1, -1):
#     print((byte >> i) & 1) #prints the bytes '11011001' out iteratively #

###FOR Trouble shooting ###

# use print and comments everywhere to check behavior#
# w = range(10)
# tot = 0
# print('***** Before the For Loop ******')
# for num in w:
#     print('***** A New Loop Iteration ******')
#     print('Value of num:', num)
#     tot += num
#     print('Value of tot:', tot)
# print('***** End of For Loop *****')
# print('Final total:', tot)

##############EXAM STUDY################################################################################################

# EXAM: email example, break into individual parts #
# EXAM: accepts user input. write function. get rid of element (either letter or number) and then combine what's left #
# EXAM: if or elif. 'print this if that. print this if not. print a long winded list of ifs and elifs #
# EXAM: tuple first part is last name and then last name reversed. DON'T OVER THINK IT. JUST HARD CODE THAT ANSWER #
# EXAM: STUDY format, reverse, sort, split, while, for, join, len, float, Dictionaries #
# EXAM: a function is not required to have a 'return' statement.  !!! hint for final !!! #
# EXAM: know how to return something asked for or 'none'. #
# EXAM: know fizzbuzz, especially the string input standardization #

#1.
''' Given a basic formula, return a calculated value.
    - given the length of base1, base2, and the height, calc the area of a trapezoid. 
    Area of a trapezoid = 1/2(base1 + base2) x height.
    - the form will be provided'''

#2
'''given an ipv4 addy as a string in dotted decimal notiation, return True if the first octet is 192 and false otherwise. 
Example input of "192.168.15.5' would return True.'''

# def question(addr):
#     if 192 == int(addr.split('.')[0]):
#         return True
#     return False


#3
'''Return a list of integers from 0 through 2048  / would be  return list(range(2049))'''

#4
'''Given a string containing the name of a football team, return the number of games it has won thus far. The team will
 only be Seatle, Dallas, Atlanta, wash, or new england'''

# def question(name):
#     teams = { dicioary
#     'Dallas': 3, 'SF':, 2
#
#     }
#
#     return teams[name]

#5
'''given a full name, print that name in the following form:'''

# <first>, <middle initial>, <last>
# only include a middle initial
# print('{},{},{}'.format(first,middle[0],last)) #note the slice #

#6
'''read a string from the user and return the string after removing any rumbers, punctuation, or special characters. 
Only return uppercase and lowercase letters in the orer provided.'''

# from string import ascii_letters as LETTERS #imports this module to # #opposite of 'isdigits' v2-q9 #
# def question():
#     usr = input()
#     # return ''.join(x for x in usr if x in LETTERS) This is a way, but below is another way # ONE LINE #
#     #this is another way #
#     result = []
#     for x in usr:
#         if x in LETTERS:
#             result.append(x)
#     return ''.join(result)

#7
'''print the contents of the file whose filename is given in infile. Ensure your output is NOT double spaced.'''

# def question(infile):
#     with open(infile) as fp:
#         for line in fp:
#             print(line,end='') #cat, user_input, ispangram,text.txt
#
#     with open('infile', 'r') as source, open('outfile', 'w') as destination:
#         destination.write(source.read())


#8

'''given an email address of the form: <first>.<middle initial>.<last>@<domain>.com return the 3 of the 4 elements of 
the address as a tuple in the order that they appear in the address. Excluding the middle initial and '.com' for example, 
if given 'al.p.eistein#somedomain.com ('al', 'einstein', 'somedomain', ) should be returned (note, two parts of the address 
were excluded from the returned tuple).'''

# def question(address): #Similar to email example #
#     ls = []
#     parts = '.'.join(address.split('@')).split('.')
#     ls.append(parts[0])
#     ls.append(parts[2])
#     ls.append(parts[3])
#     return tuples(ls)


#9
'''Given a string, return a dictionary whose keys are the set of unique characters withi the string and whose values 
are the ocunt of occurance of each character. For example, if given 'hello' the retuned dict should be {'l':2, 'h':1, 'e':1, 'o':1}'''

# for c in strng:
#     d[c] = d.get(c, 0) +1

#10
'''Return a tuple consisting of the following elements in the order listed:'''

    #your first name as a string
    #your age as an integer

#11
'''Attempt to connect to the remote host specified by the given address and port using IPv4 and TCP. If the connection 
succeeds print "CONNECTED", otherwise print "FAILED"'''

#import socket
#def question(address, port):
#     s = socket.socket()
#     try:
#         s.connect((address,port))
#     except Exception:
#         print('FAILED!')
#         return
#     print('CONNECTED')


#12
'''return the sum of all the arguments (both positional and keyword). You may assume the values are of all arguments 
are integers. iterate through a dictionary to get values'''

# def question(*args, **kwargs):
#     s = 0
#     for arg in args:
#         s += arg
#     for arg in kwargs.values():
#         s += arg
#     return s

# 13
''' connect to the server located by the given arguments using IPv4 and TCP. Send the bytes object b'fire'. 
Receive and print the response from teh server as a bytes or bytearray object. You will receive zero bytes from the 
socket.recv function when the entire message has been received.'''

# def question(address, port):
#     payload = bytearray()  # extend this bytearray with data received until 0 bytes received
#
#     s = socket.socket()  # use default #
#     s.connect((address, port))
#     msg = bytearray()  # extend this bytearray with data received until 0 bytes received
#     data = s.recv(1)
#     while data:
#         msg.extend(data)
#         data = s.recv(1)
#     print(msg)
#     return msg

#14
'''Create a class with specific functions. Create a class named baloon. Baloon instances should store a current altitude 
and allow setting of the altitude
#don't forget to include (self) as an argument in each function'''

#15
'''create and return a number whose bits are set according to the following conditions:
#a. if the filename parameter is blnank, set bit 0x1 in the return.
#b. if the admin parameter contains  a value which evaluates to True, set bit 0x10
#c. if the capacity parameter is greater that 5million, set bit 0x20'''

# def question(filename, administrator, capacity):
#     ret = 0
#     if filename == '':
#         ret |= 0x1
#     if administrator:
#         ret |= 0x10
#     if capacity > 5000000: #be sure to check for those commas #
#         ret |= 0x20
#     return ret


