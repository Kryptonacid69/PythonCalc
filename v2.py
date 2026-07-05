# Bit late but i started 28/05/2026 - not my finest moment tbh
Table = []
def TotalVariables():
  while True:    
    try:
       userCount = int(input("Enter Your Number of Variables: "))       
    except ValueError:
       print("KILL YOURSELF")
       continue
    else:     
       break
  return userCount

def GetValues():  
  Count = 0
  TotalValues = TotalVariables()
  while True and TotalValues > Count:
    try:
       userInput = float(input("Enter a Number: "))       
    except ValueError:
       print("KILL YOURSELF")
       continue
    else:
       print("TY twin")
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
'''
def SimpleSquareRooting():
   RootTable = []
   while len(Table) > 0:
      if len(RootTable) < 1 and len(Table) > 0:
         RootTable.append(Table[0])
         Table.pop(0)
      if len(Table) > 0:
         RootTable[0] = RootTable[0] / Table[0]
         Table.pop(0)
   print(f'This is all your numbers divided {RootTable[0]}')
   return RootTable[0]
'''
def OperatorOfChoice():
   userInput = input("Please Select an Operator │ +, -, *, /, ^ │: ")
   userInput = userInput.replace(" ","")
   GetValues()   
   while userInput != "+" or "-" or "*" or "/" or "^":
     if userInput == "+":
        SimpleAddition()
        break
     elif userInput == "-":
        SimpleSubtraction()
        break
     elif userInput == "*":
        SimpleMultiplication()
        break
     elif userInput == "/":
        SimpleDivision()
        break
     elif userInput == "^":
        SimpleExponentiation()
        break
     else:
        print("Please Select a Valid Operator")
        continue

OperatorOfChoice()