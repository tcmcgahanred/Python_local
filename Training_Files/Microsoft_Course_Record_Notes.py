#start with bang/bash #!/usr/bin/env python3

###displayingtext###
###stringvariables###
###storingnumbers###
###workingwithdatesandtimes###
###decisionmaking###
###complexdecisionmaking###
###repeating events###
###RepeatingEventsUntilDone###
###RememberingLists###
###savinginformationinfiles###
###ReadingFromFiles###
###Functions###


###displayingtext#########################################

print('The capybara is the worlds largest rodent')
print("the capybara likes to live in peace")
print('the capbara can swim')
print("it's a beautiful day  in the neighborhood")
# make sure you don't enclose a line of text on accident by using the wrong quotation
print('hickory dickory dock!\nthe mouse went up the clock')
# /n lets you print eveything on one line but it'll create a space whereever you put the \n ("escape character")

print('the capybara lives in \n South America')

# use ‘’’ some text ‘’’ to comment to multiple lines#

print('''you
can
split
this
way as well ''')

print("here is a string " + " here is more")

# the + sign lets you connect multiple strings#

print('what does \t do?')

# \t tabs out

# what if the text you're trying to print starts with a \? You have to put a second \ in front of it.
# I am inserting a \\ so the \ appears correctly in the string

print('I wanted the \\news to print correctly so I added a second one')

print(
    'There once was a movie star icon\nwho preferred to sleep with the light on.\nThey learned how to code\na device that sure glowed\nand lit up the night using Python!')

###stringvariables##############################

'''LEGB 
Local, Enclosing, Global, Built-in variables'''

x = 'global x' #this is a global variable because it's in the main body and can be called
#from anywhere in the program#

def test_function():
    y = 'local y' #local variable, because it's local to this 'test' function#
    #print(y)
    print(y)

test_function()
print(x)

'''m = min([5, 1, 4, 2, 3])
print(m)'''

def outer():
    # x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)

#input#
name = input("What is your name?")

# user will be prompted to type in their name, which will be passed into the ‘name’ variable#

print("Hello" + name)

country = input("What country do you live in?")

country = country.upper()  # this will capitalize the country’s name#
country = country.lower()  # this will make the 'country' variable input all lowercase#
#good for equalizing input for if statements later#

print("I live in" + country)  # country’s name should be capitalized#

message = "Hello world"
print(message.find("world"))  # find’s the position of the word “world”#
print(message.count("o"))  # find’s the position of the first ‘0’#
print(message.capitalize())
print(message.replace("Hello", "Hi"))  # replaces Hello with Hi#

#standardize input#

country = input("Where are you from?")

if country.lower() == 'canada':
    print('Oh look a Canadian.')
else:
    print('You must be American then.')

###########################

###storing numbers###################################

age = 35
print(age)

width = 12
height = 24

area = width * height
print(area)

# calculate the area of a triangle

area = width * height / 2
print("the area of the triangle would be" + area)
# ^This string will not work because "area" is a number. You can't connect a variable to a number.
# To make it work, see next string)
print("The area of the triangle would be %.2f" % area)
# The % symbol is a place holder.
# d is for decimal
# The .2 denotes how many spots there is after the decimal.
# The "f" is a float.



###working with dates and times#################################################

import datetime

currentDate = datetime.date.today()

print(currentDate)

print(currentDate.day)  # can replace "day" with "year" or "month"

import datetime

currentDate = datetime.date.today()
print(currentDate.strftime('%d %b, %y'))

print(currentDate.strftime('%d %b %y'))

userInput = input('Please enter your birthday ')
birthday = datetime.datetime.strptime(userInput,
                                      '%M/%d/%Y')  # uppercase Y is for a four digit year. Lower case is for a two digit year. uppercase M is for two digit month.
print(birthday)  # format for input needs to be x/xx/xxxx

###decision making#######################################


answer = input("Would you like a sammich?")
if answer == "yes":  # Don't forget about the == and the :.
    # Also, I need to convert the variable input into a number. Use "float". See module 2.
    print("I will make you one. I hope you like corned beef")  '''Don't forget the indent. 
    These will only print if the user selects "yes"'''
else:
    print('That\'s too bad')
# != is equal to                    / if answer == "yes" :
# == is not eqaul to                / if answer != "no" :
# < is less than                    / if total < 100 :
# > is greater than                 / if total > 100 :
# <= is less than or equal to       / if total <= 100 :
# >= is great than or equal to      / if total >= 100 :
# to convert the input from a number to a proper variable, use "float(input())

deposit = int(input("How much would you like to deposit?"))
if deposit > 100:
    print("Enjoy your free toaster!")
else:
    print("Enjoy your free mug!")
print("Have a nice day!")

# Also, I need to convert the variable input into a number. Use "float" or "int". See module 2.
# else will work if it doesn't match the if statement.

deposit = input("Would you like to make a donation?")
if float(deposit) > 100:
    # Set the boolean variable freeToaster to True
    # a boolean variable remembers the string. For instance, it'll remember "if deposit < 100: print ("enjoy your free toaster")
    freeToaster = True
# if the variable freeToaster is True the print statement will execute
if freeToaster:
    print("Enjoy your free toaster.")
else:
    print('Thats too bad')

freeToaster = False
deposit = float(input("How much would you like to deposit? "))
if deposit > 100:
    freeToaster = True

if freeToaster:
    print("Enjoy your toaster")
print("Have a nice day!")

###complexdecisionmakin / comparison operators##################################


## elif means else if
country = input("Where are you from?")

if country.lower() == "canada":  # The process will check these sequentially. Order matters.
    print("Hello")
elif country.lower() == "germany":
    print("Guten Tag")
elif country.lower() == "france":
    print("Bonjour")
else:  # in case they enter something that doesn't match up.
    print("You're not welcome here!")

team = input("Enter your favorite hockey team:").upper()
elif
if team.lower() == "flyers":
    print("Best team ever!!")
elif team.lower() == "senators":
    print("Go Sens Go!")
elif team.lower() == "rangers":
    print("Go Rangers")
else:
    print("I don\'t have anything clever to say here")

# and

sport = input("Enter your favorite sport: ").upper()
team = input("Enter your favorite hockey team:").upper()

if sport.lower() == "hockey" and team.lower() == "rangers":
    print(" YAY! ")
else:
    print(" Who cares... ")

#or command#

sport = input("Enter your favorite sport: ").upper() #standardize input with .upper()#
team = input("Enter your favorite hockey team:").upper() #not HOCKEY and RANGERS below#

if sport == "HOCKEY" and team == "RANGERS":
    print(" YAY! ")

elif team == "LEAFS" or team == "SENATORS": #elif with or#####
    print("Good luck getting the cup this year!")
else:
    print(" Who cares... ")

# if the sport is hockey, and the team is the senators or leafs, display the cup message

team = input("Enter your favorite hockey team:").upper()
sport = input("Enter your favorite sport: ").upper()

if sport == "HOCKEY" and (team == "Senators" or team == "LEAFS"): #not the use of or within the parentheses#
    print("Good luck getting into the cup this year")

# below is an example of the above problem but with flags.#

team = input("Enter your favorite hockey team:").upper()
sport = input("Enter your favorite sport: ").upper()

sportIsHockey = False
if sport == "HOCKEY":
    sportIsHockey = True

teamIsCorrect = False
if team == "SENATORS" or team == "LEAFS":
    teamIsCorrect = True

if sportIsHockey and teamIsCorrect:  # *Same as example of above with flags
    print("Good luck getting into the cup this year")

# see 46:20 in video "Complex decision making" for great example of flagging

# nesting ifs

team = input("Enter your favorite hockey team:").upper()
sport = input("Enter your favorite sport: ").upper()

if sport == "HOCKEY":
    print("Go Hockey")
    if team == "SENATORS":
        print("Good luck with getting to the cup")
    print("We do love hockey!!")

# to test this lesson, indent the last print then input different variations of words


###repeating events###


# turtle is a way to repeat events in python

import turtle

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.color("red")
turtle.left(100)
turtle.forward(100)

##to draw a box with turtle, you're essentially using the same two line
##over and over. Loops will allow you to repeat those lines.

##for command

import turtle

for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.color("red")
turtle.forward(200)

##"for" is the range of repeats
## "steps" is a variable. It could have been any word. But the word "Steps" worked well in this case.
##tab in the last two lines to see how indents matter
##"method" and "function" are interchangeable terms in coding


import turtle

for steps in range(5):
    turtle.forward(100)
    turtle.right(360 / 5)
    for moresteps in range(5):
        turtle.forward(50)
        turtle.right(360 / 5)
turtle.left(90)
turtle.forward(100)

##injecting a variable. In this case (nbrSides) or number of sides

import turtle

nbrSides = 6  # nbrSides is a variable that can be anything
turtle.forward(200)
for steps in range(nbrSides):
    turtle.forward(100)
    turtle.right(360 / nbrSides)
    for moresteps in range(nbrSides):
        turtle.forward(50)
        turtle.right(360 / nbrSides)

for steps in range(1, 4):  # remember that python starts counting at 0.
    print(steps)
print("Here we go")

for steps in [1, 2, 3, 4, 5, 6]:  # these brackets replace "range"
    print(steps)

import turtle

for color in ["red", "blue", "green", "black"]:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

import turtle

for colour in ["red", "green", "blue", "black"]:
    turtle.color(colour)
    turtle.forward(100)
    turtle.left(90)

# you can change data type ["black", 8]
# you'd need to change/add in a new variable type


###RepeatingEventsUntilDone###


##When you want something to repeat or loop
##and you don't know how many times.

# WHILE command

##do something WHILE a condition is true
##while something is true, keep doing the action (i.e. repeat/loop)

answer = "0"
while answer != "4":
    answer = input("What is 2 + 2? ")
print("WHOA!")

import turtle

counter = 0  # this can be changed to another number. counter = 1 etc...
while counter < 4:
    counter = counter + 1

# this outcome can be reached by using either a "for loop" or a "while loop".
# see the "remembering events" pres for the "for" tutorial.

import turtle

counter = 0
while counter < 4:
    turtle.forward(100)
    turtle.right(90)
    counter += 1  # this is the exact same thing as counter = counter + 1

import turtle

counter = 0
while counter < 3:
    turtle.forward(100)
    turtle.right(90)

# this ^ is the infine loop. It doesn't have an end.
# need the counter + 1 to add to the counter.


###RememberingLists###

guests = ["tim", "donna", "amanda", "josie"]
# print the first guest
# the first value is in position 0
print(guests[0])

scores = [78, 3, 22, 50, 69]
###print the fourth score
print(scores[3])

##index references to the location of an item on a list, or array.

guests = ["Tim", "Donna", "Amanda", "Josie"]

print(guests[0])
print(guests[1])

guests = ["Tim", "Donna", "Amanda", "Josie"]
# change the first value in the list to Greg
guests[0] = "Greg"
print("first value is now " + guests[0])

##add a new value to the end of the list
guests.append("Chris")

# display the last value in the list
print(guests[-1])

# delete the first time in the list
del guests[0]

guests = ["Tim", "Donna", "Amanda", "Josie"]
for steps in range(4):
    print(guests[steps])

###savinginformationinfiles###

myFile = open(fileName, accessMode)

# file types such as data.txt or mytimes.csv (csv is use for MS excel conversion)
# to get to the file, right click the file name tab up above, and select " Open containing folder"
# access mode
# r for read the file
# w for write the file
# a for append to the existing file content
# b open a binary file
# w+ or r+ read AND write to the file

fileName = "GuestList.text"
accessMode = "W"
myFile = open(fileName, accessMode)

fileName = "demo.txt"
accessMode = "w"
READ = "r"  # better than using something like accessMode = "w"

file = open(fileName, mode="w")

# better way to write this would be

fileName = "demo.txt"
WRITE = "w"
APPEND = "a"  # this will continually add to the end of the text within the document.

file = open(fileName, mode=APPEND)

# remember to close your files. A good way to remember is to write:
myFile = open(fileName, accessMode)
myFile = close()
# ..and then fill in your code in between the open and close lines.

fileName = "demo.text"
WRITE = "w"
APPEND = "a"

file = open(fileName, mode=WRITE)
file.writelines("This is the first line\n")
file.writelines("This is the second line\n")
file.close()

print("File written successfully")

# w+ or r+ will allow you to read and write onto a document

# for creating a csv file (excel doc)

fileName = "csvforexceldemo.csv"  # ensure this specifies csv
WRITE = "w"
APPEND = "a"

file = open(fileName, mode=WRITE)
file.writelines("Timothy, 35\n")  # seperate column of excel doc with commas
file.writelines("Donna, 45\n")
file.writelines("Amanda, 17\n")
file.close()

print("File written successfully")

# open containig folder and find excel doc.


###ReadingFromFiles###

fileContent = myFile.read()  # this'll dump all the contents of file below. ALL the contents.

fileContent = myFile.readline()  # this'll dump the designated line below.

animalFile = open("Tasmania.txt", "r")  # to open my file
allFileContents = animalFile.read()

print(allFileContents)

animalFile = open("Tasmania.txt", "r")  # to open my file

firstAnimal = animalFile.readline()  # to choose a line to print
print(firstAnimal)
secondAnimal = animalFile.readline()
print(secondAnimal)

###Functions###

# one of the problems with code is you're doing the same things over and over again.
# functions reduce this
# creates a button that does work for me. Just gotta load/teach the button.
# it's a named command that does somethin/"method"
# ensure the name of the function matches the method
# "read" is an example of a function; built into Python.
# ”return” returns a value back to whatever called for a value


Def
say_hi(name, age):
Print(“Hello “ + name + “, you
are “ + age)
Say_hi(“Mike”, “35”)
Say_hi(“Steve”, “70”)

def printMessage():
    print("Hello World")
    return


printMessage()


def main():
    printMessage()
    return


main()  # execute the main function. In order to do that the function must be created


def cube(num):
    return num * num * num


result = cube(4)
print(result)


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


### GUESSING GAME###
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:  # if the guess count is greater than the limit, end#
        guess = input("Enter guess: ")
        guess_count += 1  # increments the guess count#
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("YOU WIN!")


###Exponent Function###
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2, 3))

###2D Lists & Nested Loops###
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])

# will produce a 1, since it's column 0 and row 0#

###nested loop###
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:  # "row" could be any descriptor"#
    for col in row:  # "col" is column#
        print(col)  # prints out 1 though 0#


###translator###
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

###try and except### ###(Useful for avoid errors. Let’s the user know they entered in something invalid instead of breaking the program)### ###always except for a specific error###
try:
    value = 10 / 0  # this is just here to show that below, you can except #
    # a specific error instead of something so broad#
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError:
    print("Divided by zero")  # this corresponded to the "value = 10/0" above, which creates the error#
except ValueError:  # if the user enters something invalid, this will catch it#
    print("Invalid input")

###reading external files###
employee_file = open("employees.txt", "r")  # r for read, w for write, a for append, r+ for both#
for employee in employee_file.readlines():  # *#
    print(employee)
# * "readable" fill give true/false confirmation#
# * readline will read a given line (or the first by defualt#
# * readlines is better#

employee_file.close()  # always want to close files#
###write to file### add Toby ###
employee_file = open("employees.txt",
                     "a")  # w would overwrite the entire file or create new file# increment file name and create new file with w#
employee_file.write("\nToby - Human Resources")  # using \n to space down#
employee_file.write("\nKelly - Customer Service")  # using \n to space down#
employee_file.close()

###modules and pipe###
import \
    useful_tools  ###this implies that you have a module or file called “Useful Tools”, which’ll allow you to use the tool below###

print(useful_tools.roll_dice(10))

###classes and objects ###
from student import student  # from the student file i want to import the student class#

# now we'll create an object from the student class#

student1 = student("Jim", "Business", 3.1,
                   False)  # this is effectively the student object. It's an instance of the class#
student2 = student("Tim", "IT", 4.0, False)  # this is effectively the student object. It's an instance of the class#

print(student1.gpa)
print(student2.gpa)


###Multiple Choice Quiz###

# question.py#
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# game#
from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),

]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)


###Object Functions###
class student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


from student import student

student1 = student("Oscar", "Accounting", 3.1)
student2 = student("Phyllis", "Business", 3.8)

print(student2.on_honor_roll())

###inheritance###
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()


# chef#

class Chef:
    def make_chicken(self):
        Print("Chicken")

    def make_salad(self):
        print("Salad")

    def make_special_dish(self):
        print("Special dish")


# ChineseChef#

from Chef import Chef


class ChineseChef(Chef):

    def make_fried_rice(self):
        print("Fried rice")


###binary to dec or dec to binary###

def convert(fromNum, fromBase, toBase):
    toNum = 0
    power = 0
    while fromNum > 0:
        toNum += fromBase ** power * (fromNum % toBase)
        fromNum //= toBase
        power += 1
    return toNum


print(str(convert(101011, 2, 10)))
print(str(convert(126, 10, 2)))

###tictactoe###
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0], ]

print("   a  b  c")
for count, row in enumerate(game):
    print(count, row

          )

###Sears Tower exercise###

# sears.py
bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2
print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)


###Triggered####

friends = ['Tom', 'Ryan', 'Irene', 'George', 'Geoffrey', 'Eric', 'Rob', 'Ed', 'Debs']
for nonsense in range(len(friends)):
        print(friends[nonsense][0])

#####################

###tuples###

#Analogy: A single row in a database table

contact = ('David Beazley', 'dave@dabeaz.com')
stock = ('GOOG', 100, 490.1)
host = ('www.python.org', 80)

s= ('GOOG', 100, 490.1)
#to change something in the tuple, use something like
#s = (s[0], 75, s[2])
name = s[0]
shares = s[1]
price = s[2]

name, shares, price = s

print('Cost', shares * price)

#####################################

###dictionaries###

s = {
    'name' : 'GOOG',
    'shares' : 100,
    'price' : 490.1
    }

s['shares'] = 75 #change value
s['date'] ='6/6/2019'

print(s)
print(s['name']) #print a value#

##############################

### ###

#FIZZBUZZ######################

#I muddled my way to this answer#

# user_input = int(input('Give me a number:'))
#
# if user_input%15 == 0:
#      print('Multiple of 15!')
# elif user_input%5 == 0:
#     print('Multiple of 5!')
# elif user_input%3 ==0:
#     print('Multiple of 3!')
# else:
#     print('Nope')

###############################################################

#this is based on Chris's#

# user_input = int(input("Enter a number:")
#
# if user_input%15 == 0:
#     print("Fizzbuzz")
# elif (user_input) % 3) ==0:
#     print('Fizz')
# elif (user_input) % 5) == 0:
#     print('Buzz')
# else:
#     print(User_input)

##########################################################

####THIS WORKS. THIS IS THE VERSION INSTRUCTOR GAVE US FOR FIZZBUZZ#######

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

##############

###Alternate instructor's version for one-liner purposes######

# i = int(input('Enter a positive number: '))
# print(not i%15 and 'fizzbuzz' or not i%3 and 'fizz' or not i%5 and 'buzz' or i)

