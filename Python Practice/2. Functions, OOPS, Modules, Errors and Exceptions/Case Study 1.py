# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:52:30 2021

@author: saqla
"""

'''
1.A Robot moves in a Plane starting from the origin point (0,0). The robot can 
move toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given 
following:UP 5DOWN 3LEFT 3RIGHT 2.The numbers after directions are steps. 
Write a program to compute the distance from current position after sequence of 
movements.
Hint: Use math module.
'''


import math

x,y = 0,0

while True:
    steps = input("Enter UP/DOWN/LEFT/RIGHT and # of steps:")
    
    if steps == "CALCULATE":
        break
    else:
        step = steps.split()
        
        if step[0] == "UP":
            y += int(step[1])
        elif step[0] == "DOWN":
            y -= int(step[1])
        elif step[0] == "LEFT":
            x -= int(step[1])
        elif step[0] == "RIGHT":
            x += int(step[1])
        else:
            pass

distance = math.sqrt(x**2 + y**2)

print("Distance from origin is:", round(distance))


##############################################################################
'''
2.Data of XYZ company is stored in sorted list. Write a program for searching 
specific data from that list.
Hint: Use if/elif to deal with conditions.
'''

def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

item_list = [1,2,3,3,5,5,8]
item = int(input("Enter item to find:"))

if item in item_list:
    print("Item found:",binary_search(item_list,item),"\nFound at index:",item_list.index(item))
else:
    print("Item not found")
            

####################################### OR #####################################
'USING BISECT FUNCTION'


from bisect import bisect_left

def Binarysearch(item_List,item):
    i = bisect_left(item_List,item)
    if i != len(item_List) and item_List[i] == item:
        return i
    else:
        return -1



item_List = [1,3,5,7,9]
item = int(input("Enter item to find:"))

result = Binarysearch(item_List, item)
if result == -1:
    print(item,"not found")
else:
    print("First occurence of",item,"Found at index",result)


###############################################################################

'''
3.Weather forecasting organization wants to show is it day or night. 
So, write a program for such organization to findwhether is it dark outside 
or not.
Hint: Use time module.
'''

import time 

my_time = time.localtime()

if 6<=my_time.tm_hour<=18:
    print("It is day")
else:
    print("It is night")


###############################################################################

'''
4.Write a program to find distance between two locations when their latitude 
and longitudes are given.
Hint: Use math module.
'''
from math import radians, sin, cos, acos

def distance(latitude1,longitude1,latitude2,longitude2):
    
    lat1 = radians(latitude1)
    lat2 = radians(latitude2)
    lon1 = radians(longitude1)
    lon2 = radians(longitude2)
    
    dist = 6371.01 * acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon1 - lon2))
    
    print("The distance between Bangalore and Toronto is:",round(dist,2),"km")


result = distance(12.9791198,77.5912997,43.6534817,-79.3839347)


##############################################################################

'''
5.Design a software for bank system. There should be options like cash withdraw,
cash credit and change password. According to user input, the software should 
provide required output.
Hint: Use if else statements and functions.
'''
 
balance = 0

def Main():
    print("Welcome to XYZ Bank")
    global balance
    PIN = int(input("Please enter PIN number:"))
    if PIN == 1234:
        print("Please choose from the options below:\n 1:Account Balance\n 2:Cash Deposit\n 3:Cash Withdrawal\n 4:Password Change")
        option = int(input("Enter your option:"))
        if option == 1:
            Account_Balance()
        elif option == 2:
            Cash_Deposit()
        elif option == 3:
            Cash_Withdrawal()
        else:
            Password_Change()
    
    else:
        print("Please enter a valid PIN number!")
            
        
def Account_Balance():
    print("Your balance is:",balance)

def Cash_Deposit():
    global balance
    amount = float(input("Enter amount to be deposited:"))
    balance += amount
    print("Amount deposited:",amount)
    print("Your current balance is:",balance)

def Cash_Withdrawal():
    global balance
    amount = float(input("Enter amount to be withdrawn:"))
    if balance >= amount:
        balance -= amount
        print("You withdrew:",amount)
        print("Your current balance is:",balance)
    else:
        print("You have Insufficient Balance!")

def Password_Change():
    old_password = str(input("Please enter your old password:"))
    if old_password == 'abc123':
        new_password = str(input("Please enter your new password:"))
        print("Your new password is:",new_password)
    else:
        print("You entered an incorrect old password")


Main()
           
        
##############################################################################

'''
6.Write a program which will find all such numbers which are divisible by 7 but
are not a multiple of 5, between 2000 and 3200 (both included). The numbers 
obtained should be printed in a comma-separated sequence on a single line.        
'''

x = list(filter(lambda x: x%5 != 0, range(2000,3201)))

result =[]

for i in list(filter(lambda num: num%7==0,x)):
    result.append(str(i))
    
print(",".join(result))

##############################################################################

'''
7.Write a program which can compute the factorial of a given numbers. Use 
recursion to find it. 
Hint: Suppose the following input is supplied to the program:8
Then, the output should be:40320
'''

def factorial(num):
    if num<0:
        print("Invalid input!!")
    elif num==0 or num==1:
        return 1

    else:
        return num*factorial(num-1)
    
    

num = int(input("Enter a number:"))
print("Factorial of",num,"is",factorial(num))

##############################################################################

'''
8.Write a program that calculates and prints the value according to the given 
formula:Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30.D  is  the  
variable  whose  values  should  be  input  to  your  program  in  a  
comma-separated sequence. 
Example:Let  us  assume  the  following  comma  separated  input  sequence  is 
given  to  the program:100,150,180The output of the program should be:18,22,24
'''

from math import sqrt

C,H = 50,30

D = input("Enter the input sequence:")
items = D.split(',')

result = []

for value in items:
    Q = round(sqrt((2*C*float(value))/H))
    result.append(str(Q))

print('Output is:',",".join(result))

##############################################################################

'''
9.Write a program which takes 2 digits, X,Y as input and generates a 
2-dimensional array. The element value in the i-th row and j-th column of the 
array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡-Y-1.
Example:Suppose the following inputs are given to the program:3,5
Then, the output of the program should be:
  [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''

X,Y = input("Enter the number of rows and columns:").split(",")
X = int(X)
Y = int(Y)

multi_list = [[0 for col in range(Y)] for row in range(X)]

for row in range(X):
    for col in range(Y):
        multi_list[row][col]= row*col

print(multi_list)
print("2-D array is:")

for x in multi_list:
    print(x)
    
##############################################################################

'''
10.Write a program that accepts a comma separated sequence of words as input 
and prints the words in a comma-separated sequence after sorting them 
alphabetically. Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:bag,hello,without,world
'''

words = input("Enter the comma separated sequence of words:").split(",")

sorted_words = sorted(words)
print('Output:',",".join(sorted_words))


##############################################################################

'''
11.Write a program that accepts sequence of lines as input and prints the lines
after making all characters in the sentence capitalized. Suppose the following
inputis supplied to the program:Hello world \n Practice makes perfect. Then, 
the output should be: HELLO WORLD PRACTICE MAKES PERFECT
'''

result =[]

while True:
    string = input("Enter strings:")
    
    if string:
        result.append(string.upper())

    else:
        break

for word in result:
    print(word)

##############################################################################

'''
12.Write a program that accepts a sequence of whitespace separated words as 
input and   prints   the   words   after   removing   all   duplicate   words  
and   sorting   them alphanumerically. Suppose the following input is supplied
to the program:hello world and practice makes perfect and hello world again.
Then, the output should be:again and hello makes perfect practice world
'''

words = input("Enter a sentence:").split()

remove_duplicates = list(set(words))

sorted_sequence = sorted(remove_duplicates)

print("Output is:"," ".join(sorted_sequence))

##############################################################################

'''
13.Write  a  program  which  accepts  a  sequence  of  comma  separated  4  
digit  binary numbers  as  its  input  and  then  check  whether  they  are  
divisible  by  5  or  not.  The numbers that are divisible by 5 are to be 
printed in a comma separated sequence.
Example:0100,0011,1010,1001
Then the output should be:1010
'''

binary_numbers = input("Enter a sequence of binary numbers:").split(",")

result = [bin_num for bin_num in binary_numbers if int(bin_num,2)%5 == 0]

print("Output:",",".join(result))
            
##############################################################################

'''
14.Write  a  program  that  accepts  a  sentence  and  calculate  the  number 
of  upper  case letters and lower case letters.Suppose the following input is 
supplied to the program:Hello world!Then, the output should be:
UPPER CASE 1 LOWER CASE 9
'''
sentence = input("Enter a sentence:")

UPPER_CASE = 0
LOWER_CASE = 0

for i in sentence:
    if i.isupper():
        UPPER_CASE +=1
    elif i.islower():
        LOWER_CASE +=1
    else:
        pass

print("UPPER CASE:",UPPER_CASE)
print("LOWER CASE:",LOWER_CASE)

##############################################################################

'''
15.Give example of fsum and sum function of math library.
'''
import math 

#list

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
list3 = [1.5,2.5,5.06]

sum(list1)
math.fsum(list1)

sum(list2)
math.fsum(list2)

sum(list3)
math.fsum(list3)

#range

sum(range(10))
math.fsum(range(10))
