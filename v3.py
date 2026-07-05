# Bit late but i started 28/05/2026 - not my finest moment tbh
import os
Table = []
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

TotalEquation = "Test"
# Done on 29/05/26, getting directory stuff working
def WriteResultsToFile():
   check = ["y", "n"]
   YesNo = input("Would you like to Save the Calculation to a .TXT file? Y/N ").lower()
   while YesNo not in check:
     YesNo = input("Would you like to Save the Calculation to a .TXT file? Y/N ").lower()
   if YesNo in check:
     if YesNo == "y":
       file = open(os.getcwd(), "a")
       file.write(TotalEquation + "\n")
       file.close()      
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

def SimpleMultiplication():
   MultTable = []
   while len(Table) > 0:
      if len(MultTable) < 1 and len(Table) > 0:
         MultTable.append(Table[0])
         Table.pop(0)
      if len(Table) > 0:
         MultTable[0] = MultTable[0] * Table[0]
         Table.pop(0)
   print(f'This is all your numbers multiplied: {MultTable[0]:g}')
   return MultTable[0]

def SimpleDivision():
   DivideTable = []
   while len(Table) > 0:
      if len(DivideTable) < 1 and len(Table) > 0:
         DivideTable.append(Table[0])
         Table.pop(0)
      if len(Table) > 0:
         DivideTable[0] = DivideTable[0] / Table[0]
         Table.pop(0)
   print(f'This is all your numbers divided: {DivideTable[0]:g}')
   return DivideTable[0]

def SimpleAddition():
   TotalSum = sum(Table)
   print(f"The Total Sum of all your numbers is: {TotalSum:g}")
   return TotalSum 

def SimpleSubtraction():
   SubTable = []
   while len(Table) > 0:
      if len(SubTable) < 1 and len(Table) > 0:
         SubTable.append(Table[0])
         Table.pop(0)
      if len(Table) > 0:
         SubTable[0] = SubTable[0] - Table[0]
         Table.pop(0)
   print(f'This is all your numbers subtracted: {SubTable[0]:g}')
   return SubTable[0]

def SimpleExponentiation():
   ExpoTable = []
   while len(Table) > 0:
      if len(ExpoTable) < 1 and len(Table) > 0:
         ExpoTable.append(Table[0])
         Table.pop(0)
      if len(Table) > 0:
         ExpoTable[0] = ExpoTable[0] ** Table[0]
         Table.pop(0)
   print(f'This is all your numbers to the power of each other: {ExpoTable[0]:g}')
   return ExpoTable[0]

def SimpleRooting():
   RootTable = []
   while len(Table) > 0:
      if len(RootTable) < 1 and len(Table) > 0:
         RootTable.append(Table[0])
         Table.pop(0)
      if len(Table) > 0:
         RootTable[0] = RootTable[0] ** (1 / Table[0])
         Table.pop(0)
   print(f'This is all your numbers rooted {RootTable[0]:g}')
   return RootTable[0]

def OperatorOfChoice():
   OperatorTable = ["+","-","*","/","^","Root"]
   userInput = input("Please Select an Calculation │ +, -, *, /, ^, Sqrt │ ")
   while userInput not in OperatorTable:
      userInput = input("Not a Valid Calculation. Please Try Again │ +, -, *, /, ^, Sqrt │ ")
   
   if userInput in OperatorTable:
      GetValues()     
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

OperatorOfChoice()
