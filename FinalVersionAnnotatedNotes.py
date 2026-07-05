# Important Python Modules that need to exist for code to work

import os
import math

# a couple of useful tables and variables that do better outside of the functions

Table = []
Operator = ""
FinalAnswer = 0

# first function, gets userinput to get the amount of numbers that are being operated on,
# i.e if the number is three, X * X * X = X, or 2 X * X = X

def TotalVariables():
  
  # loop that repeats infinitely until they enter A NORMAL FUCKING NUMBER
  # if their number is negative, or infinity/ a Non - Integer, the code repeats
  # asking to get the amount of numbers to calculate

  while True:    
    try:      
       # asks user for amount of numbers, and asserts that the number must be above 0
       userCount = int(input("Enter the Amount of Numbers To Calculate: ")) 
       assert userCount > 0   
    except AssertionError:
       # if the number is below 1, continues asking for a number
       print("Please enter a Number Greater than 0")
       continue   
    except ValueError:
       # if the input is not a real number, continues asking for a number
       print("Please enter a real Number")
       continue
    else:           
   # the break that ends to loop to allow the calculator to continue
       break
  return userCount

# second function, not in chronological order but idrc. function asks the user if they want to save
# the calculation results to file, otherwise doesnt
def WriteResultsToFile():
   # small table for comparisons, a yes / no check of sorts
   check = ["y", "n"]
   # gets the directory for the users computer name, allowing it not to work on just my computer
   StartOfDirectory = os.path.expanduser('~')
   # Yes/no check to ask if user wants to save the calculation
   YesNo = input("Would you like to Save the Calculation to a .TXT file? Y/N ").lower()
   while YesNo not in check:
     # loops until a y/n is given, using the check table
     YesNo = input("Please Choose a Valid Answer: Y/N ").lower()
   # checks what the input was, and makes the outcome based on that
   if YesNo in check:
     if YesNo == "y":
       # if the check is yes, concatenates a path to make the calculation txt file appear on the desktop.
       # it will append new things to the file on a new line, and the encoding thing is for a non-standard
       # character, the root symbol in this case
       with open(StartOfDirectory + "\\" + "Desktop\\Calculations.txt", "a", encoding="utf-8") as CalcSave:
         # appends the total equation, returned from the total equation function, and lets the user know its saved
         CalcSave.write(TotalEquation() + "\n")   
       print("Please Check Your Main Desktop For Your .TXT File Log")
     else:
        # if the outcome is N, which is the only other option, ends the function
        print("Thank You For using the calculator")

# Third function, to get the users number they want to calculate. works by adding numbers to a table
# i.e if user entered 2, 43, and 90 they would be entered as a table like [2, 43, 90]
def GetValues():
  # Count variable of the total amount of numbers the user wants to get  
  Count = 0
  # count variable becomes the returned result from the TotalVariables() function
  TotalValues = TotalVariables()
  # Standard loop, yeah i use these alot
  while True and TotalValues > Count:
    # asks for a float, so the calculator can use all kinds of numbers including decimals
    try:
       userInput = float(input("Enter a Number: "))       
    except ValueError:
       # if the value is a non-number, asks again.
       print("Please enter a Real Number")
       continue
    else:
       # If the number is a number, appends it to a table, and increments the count by 1. this allows
       # the amount of numbers the user asked for to be given accurately
       Table.append(userInput)      
       Count = Count + 1
  return Table

# fourth function, the function that concatenates (yes i know what that word means, joinign stuff together)
# the equation into a string to be neatly exported into the txt file on the desktop

def TotalEquation():
   # table that stores the strings that make up the equation
   ConcatnenateTable = []
   # count for the loop
   Count = 0
   for i in range(len(Table) - 1):
      # loops thru the table, adding the numbers. basically adds the first number, then an operator, then the second, 
      # and so on so forth until the count exceeds the limit
      ConcatnenateTable.append(f'{Table[Count]:g} ')
      ConcatnenateTable.append(f"{Operator} ")
      Count = Count + 1
   # appends the final thing in the table, in case the user only puts one thing in
   ConcatnenateTable.append(f'{Table[-1]:g}')
   # finally, appends a =, then the final answer to complete the equation
   ConcatnenateTable.append(f' = {FinalAnswer:g} ')
   # Joins every string together into one
   FinalString = ''.join(map(str, ConcatnenateTable))
   # returns the newly concatenated string to be used elsewhere (i love that word)
   return FinalString

#so.. basically every one of these operator table thingys are basically the same thing. this means that
#im just gonna explain up here. so the function iterates thru the table of numbers that the user put in,
# and does all the calculations to make the final answer. the count starts at one incase the user only puts one number in
# making sure the string is accurate in the .txt file. the overflow error catcher is on the multiplication, division, exponential
# and root equation blocks, to make sure the user doesnt overflow the calculator. if it does, it just makes the answer infinite and
# moves on. the number is above what can be accurately stored anyway, i think its 2.2 x 10^308 ?
# the global is yucky, but it works so idrc, i dont wanna learn returns properly YOU CANT MAKE ME
def SimpleMultiplication():
   Count = 1
   Answer = Table[0]
   while len(Table) > Count:
      try:   
         Answer = Answer * Table[Count]
         Count = Count + 1
      except OverflowError:
         print("This Number exceeds INF!")
         Answer = math.inf
         break 
   global FinalAnswer
   FinalAnswer = Answer
   print(f'This is all your numbers multiplied: {Answer:g}')
   return Answer

def SimpleDivision():
   Count = 1
   Answer = Table[0]
   while len(Table) > Count:
      try:
         Answer = Answer / Table[Count]
         Count = Count + 1
      except OverflowError:
         print("This Number exceeds INF!")
         Answer = math.inf
         break 
   global FinalAnswer
   FinalAnswer = Answer
   print(f'This is all your numbers divided: {Answer:g}')
   return Answer

def SimpleAddition():
   Count = 1
   Answer = Table[0]
   while len(Table) > Count:
      Answer = Answer + Table[Count]
      Count = Count + 1
   global FinalAnswer
   FinalAnswer = Answer
   print(f'This is all your numbers added together: {Answer:g}')
   return Answer

def SimpleSubtraction():
   Count = 1
   Answer = Table[0]
   while len(Table) > Count:
      Answer = Answer - Table[Count]
      Count = Count + 1
   global FinalAnswer
   FinalAnswer = Answer
   print(f'This is the first number divided by all the others: {Answer:g}')
   return Answer

def SimpleExponentiation():
   Count = 1
   Answer = Table[0]
   while len(Table) > Count:
      try:
        Answer = Answer ** Table[Count]
        Count = Count + 1
      except OverflowError:
         print("This Number exceeds INF!")
         Answer = math.inf
         break   
   global FinalAnswer
   FinalAnswer = Answer
   print(f'This is all your numbers to the power of each other: {Answer:g}')
   return Answer

def SimpleRooting():
   Count = 1
   Answer = Table[0]
   while len(Table) > Count:
      try:   

      # i didnt use math.pi because this achieves the same thing anyway. something to the 9 ^ 1/2 equals 9 root 2,
      # so yeah this was easier.

         Answer = Answer ** (1 / Table[Count])
         Count = Count + 1
      except OverflowError:     
         print("This Number exceeds INF!")
         Answer = math.inf
         break 
   global FinalAnswer
   FinalAnswer = Answer
   print(f'This is your first number Rooted by the others: {Answer:g}')
   return Answer

# gets the operator the user wants to use. repeating ad infinitum until it gets a valid option from the OperatorTable
# another yucky global, but its fine because i dont think you know how to input a radical symbol (the square root one)
# anyway.
def OperatorOfChoice():
   # table for checking if input is what we want
   OperatorTable = ["+","-","*","/","^","Root"]
   # userinput asker
   userInput = input("Please Select an Calculation │ +, -, *, /, ^, Root │ ")
   # if its not in the table, repeat ad infinitum until their answer is
   while userInput not in OperatorTable:
      userInput = input("Not a Valid Calculation. Please Try Again │ +, -, *, /, ^, Root │ ")  
   # if it is, use a yucky global to make the operator a radical for the concatenate string, and run the
   # corrosponding operator function. also runs all the other functions to get them working.
   if userInput in OperatorTable:
      global Operator
      Operator = userInput
      if Operator == "Root":
         Operator = "√"
      GetValues()   
      TotalEquation()  
      if userInput == "+":
         SimpleAddition()
      if userInput == "-":
         SimpleSubtraction()
      if userInput == "*":
         SimpleMultiplication()
      if userInput == "/":
         SimpleDivision()
      if userInput == "^":
         SimpleExponentiation()
      if userInput == "Root":
         SimpleRooting()
      WriteResultsToFile()
      # small little loop to remove the intergers from the table every restart, to make sure the equations are accurate
      for i in range(len(Table)):
         Table.pop(0)
      RunLoop()
   # returns the operator for the concatenate table
   return userInput

# loops the calculator until the user doesnt want it anymore
def RunLoop():
   # yada yada i doubt your reading it atp and just skiming, same shit as before
   YesNoTable = ["y", "n"]
   userInput = input("Would You Like to use the Calculator?│ Y/N │ ").lower()
   while userInput not in YesNoTable:
      userInput = input("Not a Valid Input. Please Try Again │ Y/N │ ").lower()
   if userInput == "y":
      # runs calc is user wants, otherwise doesnt
      OperatorOfChoice()
   elif userInput == "n":
      print("Thank You For Using the calculator")

# the line of code holding it all together. it looks ugly and i have no clue if i should wrap it in a if statement or
# sumthing, but it works the same so eh
RunLoop()