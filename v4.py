# Bit late but i started 28/05/2026 - not my finest moment tbh
import os
Table = []
Operator = ""
def TotalVariables():
  while True:    
    try:
       userCount = int(input("Enter the Amount of Numbers To Calculate: "))       
    except ValueError:
       print("Please enter a Real Number")
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
       with open(StartOfDirectory + "\\" + "Desktop\\Calculations.txt", "a") as CalcSave:
         CalcSave.write(TotalEquation() + "\n")   
       print("Please Check Your Main Desktop For Your .TXT File Log")
     else:
        print("Thank You for coming to my ted talk")

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

# Fix stupid operator issue & also it only works with the addition as it comes after the equation
# Function pops the table and theres no more values to actually put for the file write

def TotalEquation():
   ConcatnenateTable = []
   Count = 0
   for i in range(len(Table)):
      ConcatnenateTable.append(f'{Table[Count]:g}' + " ")
      ConcatnenateTable.append(" " + Operator + " ")
      Count = Count + 1
   ConcatnenateTable.append(" " + "=" + " FinalAnswerHopefully")
   FinalString = ''.join(map(str, ConcatnenateTable))
   return FinalString

def SimpleMultiplication():
   Count = 1
   while len(Table) > Count:
      Table[0] = Table[0] * Table[Count]
      Count = Count + 1
   print(f'This is all your numbers multiplied: {Table[0]:g}')
   return Table[0]

def SimpleDivision():
   Count = 1
   while len(Table) > Count:
      Table[0] = Table[0] / Table[Count]
      Count = Count + 1
   print(f'This is all your numbers divided: {Table[0]:g}')
   return Table[0]

def SimpleAddition():
   TotalSum = sum(Table)
   print(f"The Total Sum of all your numbers is: {TotalSum:g}")
   return TotalSum 

def SimpleSubtraction():
   Count = 1
   while len(Table) > Count:
      Table[0] = Table[0] - Table[Count]
      Count = Count + 1
   print(f'This is the first number divided by all the others: {Table[0]:g}')
   return Table[0]

def SimpleExponentiation():
   Count = 1
   while len(Table) > Count:
      Table[0] = Table[0] ** Table[Count]
      Count = Count + 1
   print(f'This is all your numbers to the power of each other: {Table[0]:g}')
   return Table[0]

def SimpleRooting():
   Count = 1
   while len(Table) > Count:
      Table[0] = Table[0] ** (1 / Table[Count])
      Count = Count + 1
   print(f'This is all your numbers divided: {Table[0]:g}')
   return Table[0]

def OperatorOfChoice():
   OperatorTable = ["+","-","*","/","^","Root"]
   userInput = input("Please Select an Calculation │ +, -, *, /, ^, Root │ ")
   while userInput not in OperatorTable:
      userInput = input("Not a Valid Calculation. Please Try Again │ +, -, *, /, ^, Root │ ")   
   if userInput in OperatorTable:
      Operator = userInput
      print(Operator)
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
   return userInput

OperatorOfChoice()
