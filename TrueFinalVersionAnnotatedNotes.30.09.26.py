# Important Python Modules that need to exist for code to work

import os
import math

# a couple of useful tables and variables that do better outside of the functions

table = []
operator = ""
final_answer = 0

# first function, gets user_input to get the amount of numbers that are being operated on,
# i.e if the number is three, X * X * X = X, or 2 X * X = X

def total_variables():
  
  # loop that repeats infinitely until they enter A NORMAL FUCKING NUMBER
  # if their number is negative, or infinity/ a Non - Integer, the code repeats
  # asking to get the amount of numbers to calculate

  while True:    
    try:      
       # asks user for amount of numbers, and asserts that the number must be above 0
       user_count = int(input("Enter the Amount of Numbers To Calculate: ")) 
       assert user_count > 0   
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
  return user_count

# second function, not in chronological order but idrc. function asks the user if they want to save
# the calculation results to file, otherwise doesnt
def write_results_to_file():
   # small table for comparisons, a yes / no check of sorts
   check = ["y", "n"]
   # gets the directory for the users computer name, allowing it not to work on just my computer
   start_of_directory = os.path.expanduser('~')
   # Yes/no check to ask if user wants to save the calculation
   yes_no = input("Would you like to Save the Calculation to a .TXT file? Y/N ").lower()
   while yes_no not in check:
     # loops until a y/n is given, using the check table
     yes_no = input("Please Choose a Valid answer: Y/N ").lower()
   # checks what the input was, and makes the outcome based on that
   if yes_no in check:
     if yes_no == "y":
       # if the check is yes, concatenates a path to make the calculation txt file appear on the desktop.
       # it will append new things to the file on a new line, and the encoding thing is for a non-standard
       # character, the root symbol in this case
       with open(start_of_directory + "\\" + "Desktop\\Calculations.txt", "a", encoding="utf-8") as calc_save:
         # appends the total equation, returned from the total equation function, and lets the user know its saved
         calc_save.write(total_equation() + "\n")   
       print("Please Check Your Main Desktop For Your .TXT File Log")
     else:
        # if the outcome is N, which is the only other option, ends the function
        print("Thank You For using the calculator")

# Third function, to get the users number they want to calculate. works by adding numbers to a table
# i.e if user entered 2, 43, and 90 they would be entered as a table like [2, 43, 90]
def get_values():
  # count variable of the total amount of numbers the user wants to get  
  count = 0
  # count variable becomes the returned result from the total_variables() function
  total_values = total_variables()
  # Standard loop, yeah i use these alot
  while True and total_values > count:
    # asks for a float, so the calculator can use all kinds of numbers including decimals
    try:
       user_input = float(input("Enter a Number: "))       
    except ValueError:
       # if the value is a non-number, asks again.
       print("Please enter a Real Number")
       continue
    else:
       # If the number is a number, appends it to a table, and increments the count by 1. this allows
       # the amount of numbers the user asked for to be given accurately
       table.append(user_input)      
       count = count + 1
  return table

# fourth function, the function that concatenates (yes i know what that word means, joinign stuff together)
# the equation into a string to be neatly exported into the txt file on the desktop

def total_equation():
   # table that stores the strings that make up the equation
   concatenate_table = []
   # count for the loop
   count = 0
   for i in range(len(table) - 1):
      # loops thru the table, adding the numbers. basically adds the first number, then an operator, then the second, 
      # and so on so forth until the count exceeds the limit
      concatenate_table.append(f'{table[count]:g} ')
      concatenate_table.append(f"{operator} ")
      count = count + 1
   # appends the final thing in the table, in case the user only puts one thing in
   concatenate_table.append(f'{table[-1]:g}')
   # finally, appends a =, then the final answer to complete the equation
   concatenate_table.append(f' = {final_answer:g} ')
   # Joins every string together into one
   final_string = ''.join(map(str, concatenate_table))
   # returns the newly concatenated string to be used elsewhere (i love that word)
   return final_string

#so.. basically every one of these operator table thingys are basically the same thing. this means that
#im just gonna explain up here. so the function iterates thru the table of numbers that the user put in,
# and does all the calculations to make the final answer. the count starts at one incase the user only puts one number in
# making sure the string is accurate in the .txt file. the overflow error catcher is on the multiplication, division, exponential
# and root equation blocks, to make sure the user doesnt overflow the calculator. if it does, it just makes the answer infinite and
# moves on. the number is above what can be accurately stored anyway, i think its 2.2 x 10^308 ?
# the global is yucky, but it works so idrc, i dont wanna learn returns properly YOU CANT MAKE ME
def multiplication():
   count = 1
   answer = table[0]
   while len(table) > count:
      try:   
         answer = answer * table[count]
         count = count + 1
      except OverflowError:
         print("This Number exceeds INF!")
         answer = math.inf
         break 
   global final_answer
   final_answer = answer
   print(f'This is all your numbers multiplied: {answer:g}')
   return answer

def division():
   count = 1
   answer = table[0]
   while len(table) > count:
      try:
         answer = answer / table[count]
         count = count + 1
      except OverflowError:
         print("This Number exceeds INF!")
         answer = math.inf
         break 
      except ZeroDivisionError:
         print("That is An Undefinable Number!")
         answer = 0
         break 
   global final_answer
   final_answer = answer
   print(f'This is all your numbers divided: {answer:g}')
   return answer

def addition():
   count = 1
   answer = table[0]
   while len(table) > count:
      answer = answer + table[count]
      count = count + 1
   global final_answer
   final_answer = answer
   print(f'This is all your numbers added together: {answer:g}')
   return answer

def subtraction():
   count = 1
   answer = table[0]
   while len(table) > count:
      answer = answer - table[count]
      count = count + 1
   global final_answer
   final_answer = answer
   print(f'This is the first number subtracted by all the others: {answer:g}')
   return answer

def exponentiation():
   count = 1
   answer = table[0]
   while len(table) > count:
      try:
        answer = answer ** table[count]
        count = count + 1
      except OverflowError:
         print("This Number exceeds INF!")
         answer = math.inf
         break   
   global final_answer
   final_answer = answer
   print(f'This is all your numbers to the power of each other: {answer:g}')
   return answer

def root():
   count = 1
   answer = table[0]
   while len(table) > count:
      try:   

      # i didnt use math.sqrt() because this achieves the same thing anyway. something to the 9 ^ 1/2 equals 9 root 2,
      # so yeah this was easier.

         answer = answer ** (1 / table[count])
         count = count + 1
      except OverflowError:     
         print("This Number exceeds INF!")
         answer = math.inf
         break 
      except ZeroDivisionError:
         print("That is An Undefinable Number!")
         answer = 0
         break 
   global final_answer
   final_answer = answer
   print(f'This is your first number Rooted by the others: {answer:g}')
   return answer

# gets the operator the user wants to use. repeating ad infinitum until it gets a valid option from the operator_table
# another yucky global, but its fine because i dont think you know how to input a radical symbol (the square root one)
# anyway.
def operator_of_choice():
   # table for checking if input is what we want
   operator_table = ["+","-","*","/","^","Root"]
   # user_input asker
   user_input = input("Please Select an Calculation │ +, -, *, /, ^, Root │ ")
   # if its not in the table, repeat ad infinitum until their answer is
   while user_input not in operator_table:
      user_input = input("Not a Valid Calculation. Please Try Again │ +, -, *, /, ^, Root │ ")  
   # if it is, use a yucky global to make the operator a radical for the concatenate string, and run the
   # corrosponding operator function. also runs all the other functions to get them working.
   if user_input in operator_table:
      global operator
      operator = user_input
      if operator == "Root":
         operator = "√"
      get_values()   
      total_equation()  
      if user_input == "+":
         addition()
      if user_input == "-":
         subtraction()
      if user_input == "*":
         multiplication()
      if user_input == "/":
         division()
      if user_input == "^":
         exponentiation()
      if user_input == "Root":
         root()
      write_results_to_file()
      # small little loop to remove the intergers from the table every restart, to make sure the equations are accurate
      for i in range(len(table)):
         table.pop(0)
      run_loop()
   # returns the operator for the concatenate table
   return user_input

# loops the calculator until the user doesnt want it anymore
def run_loop():
   # yada yada i doubt your reading it atp and just skiming, same shit as before
   yes_no_table = ["y", "n"]
   user_input = input("Would You Like to use the Calculator?│ Y/N │ ").lower()
   while user_input not in yes_no_table:
      user_input = input("Not a Valid Input. Please Try Again │ Y/N │ ").lower()
   if user_input == "y":
      # runs calc is user wants, otherwise doesnt
      operator_of_choice()
   elif user_input == "n":
      print("Thank You For Using the calculator")

# the line of code holding it all together. it looks ugly and i have no clue if i should wrap it in a if statement or
# sumthing, but it works the same so eh
run_loop()