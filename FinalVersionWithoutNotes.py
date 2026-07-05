# Bit late but i started 28/05/2026 - not my finest moment tbh
import os
import math
Table = []
Operator = ""
FinalAnswer = 0
def TotalVariables():
  while True:    
    try:
       userCount = int(input("Enter the Amount of Numbers To Calculate: ")) 
       assert userCount > 0   
    except AssertionError:
       print("Please enter a Number Greater than 0")
       continue   
    except ValueError:
       print("Please enter a real Number")
       continue
    else:     
       break
  return userCount

# Done on 29/05/26, getting directory stuff working
def WriteResultsToFile():
   check = ["y", "n"]
   StartOfDirectory = os.path.expanduser('~')
   YesNo = input("Would you like to Save the Calculation to a .TXT file? Y/N ").lower()
   while YesNo not in check:
     YesNo = input("Please Choose a Valid Answer: Y/N ").lower()
   if YesNo in check:
     if YesNo == "y":
       with open(StartOfDirectory + "\\" + "Desktop\\Calculations.txt", "a", encoding="utf-8") as CalcSave:
         CalcSave.write(TotalEquation() + "\n")   
       print("Please Check Your Main Desktop For Your .TXT File Log")
     else:
        print("Thank You For using the calculator")

def GetValues():  
  Count = 0
  TotalValues = TotalVariables()
  while True and TotalValues > Count:
    try:
       userInput = float(input("Enter a Number: "))       
    except ValueError:
       print("Please enter a Real Number")
       continue
    else:
       Table.append(userInput)      
       Count = Count + 1
  return Table

def TotalEquation():
   ConcatnenateTable = []
   Count = 0
   for i in range(len(Table) - 1):
      ConcatnenateTable.append(f'{Table[Count]:g} ')
      ConcatnenateTable.append(f"{Operator} ")
      Count = Count + 1
   ConcatnenateTable.append(f'{Table[-1]:g}')
   ConcatnenateTable.append(f' = {FinalAnswer:g} ')
   FinalString = ''.join(map(str, ConcatnenateTable))
   return FinalString

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

def OperatorOfChoice():
   OperatorTable = ["+","-","*","/","^","Root"]
   userInput = input("Please Select an Calculation │ +, -, *, /, ^, Root │ ")
   while userInput not in OperatorTable:
      userInput = input("Not a Valid Calculation. Please Try Again │ +, -, *, /, ^, Root │ ")  
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
      for i in range(len(Table)):
         Table.pop(0)
      RunLoop()
   return userInput

def RunLoop():
   YesNoTable = ["y", "n"]
   userInput = input("Would You Like to use the Calculator?│ Y/N │ ").lower()
   while userInput not in YesNoTable:
      userInput = input("Not a Valid Input. Please Try Again │ Y/N │ ").lower()
   if userInput == "y":
      OperatorOfChoice()
   elif userInput == "n":
      print("Thank You For Using the calculator")

# This is the nail that holds the entire building to the ground! I wasn't joking

RunLoop()
