# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:50:07 2021

@author: saqlain
"""
###############################################################################
'''
1.What is the output of the following code?
'''

nums =set([1,1,2,3,3,3,4,4])
print(len(nums))
# output = 4

###############################################################################

'''
2.What will be the output?
'''

d ={"john":40, "peter":45}
print(list(d.keys()))
#output = ['john', 'peter']


###############################################################################

'''
3.A website requires a user to input username and password to register. 
Write a program to check the validity of password given by user. 
Following are the criteria for checking password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
'''

password = str(input("Enter a password:"))

lowercase_letter=0
Uppercase_letter=0
digit=0
special_char=0

if (6<=len(password)<=12):
    for i in password:
        if i.islower()==True:
            lowercase_letter+=1
            
        if i.isupper()==True:
            Uppercase_letter+=1
                
        if i.isdigit()==True:
            digit+=1
                    
        if i in list(('$','#','@')):
            special_char+=1
if (lowercase_letter>=1 and Uppercase_letter>=1 and digit>=1 and special_char>=1 and (lowercase_letter+Uppercase_letter+digit+special_char)==len(password)):
    print("Great! The password is valid")
else:
    print("Invalid password")
       
###############################################################################


'''
4.Write a for loop that prints all elements of a list and 
their position in the list.
'''
a = [4,7,3,2,5,9]

for i in a:
    print("{0} -> index position is {1}".format(i,a.index(i)))

###############################################################################


'''
5.Please   write   a   program   which accepts  a   string   from   console  
and   print   the characters that have even indexes.
'''

string = str(input("Enter a string:"))
output=[]

# H1e2l3l4o5w6o7r8l9d

for i in string:
    if (string.index(i))%2==0:
        output.append(i)
    else:
        pass
print("Output is :","".join(output))


###############################################################################


'''
6.Please write a program which accepts a string from console and 
print it in reverse order.
'''


string=str(input("Enter a string:"))

#rise to vote sir

print(string[::-1])


###############################################################################


'''
7.Please write a program which count and print the numbers of each character 
in a string input by console.
'''

string = (input("Enter a string:"))

count={i:string.count(i) for i in set(string)}
print("The count of characters are:",count)

        
                        ###########  OR  ###########

string = (input("Enter a string:"))
dict1={}

for i in string:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print("The count of characters are:",dict1)


###############################################################################


'''
8.With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],write a 
program to make a list whose elements are intersection of the above given lists.
'''

list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]

list3=list(set(list1).intersection(set(list2)))
print("The intersection of list1 and list2 is:",list3)


###############################################################################


'''
9.By using list comprehension, please write a program to print the list after 
removing the value 24 in [12,24,35,24,88,120,155].
'''

lst = [12,24,35,24,88,120,155]


for i in lst:
    if i==24:
        lst.remove(24)
    else:
        pass
print(lst)


###############################################################################


'''
10.By using list comprehension, please write a program to print the list after 
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''

list1 = [12,24,35,70,88,120,155]

for i in range(len(list1)):
    if i==0:
        list1.pop(i)
    elif i==3:
        list1.pop(i)
        list1.pop(i)
    else:
        pass
print(list1)
        

###############################################################################
    
'''
11.By using list comprehension, please write a program to print the list after
removing delete numbers which are divisible by 5 and 7 in 
[12,24,35,70,88,120,155].
'''

lst = [12,24,35,70,88,120,155]
new_list = []

for i in lst:
    if not ((i%5==0) and (i%7==0)):
        new_list.append(i)
    else:
        pass

print(new_list)


###############################################################################

'''
12.Write  a  program  to  compute  (1/2)+(2/3)+(3/4)+...+(n/n+1)  with  a  
given n  input  by console (n>0).
Example:
 If the following n is given as input to the program: 5
 Then, the output of the program should be: 3.55

'''

result=0
console_input = int(input("Enter a number:"))

if console_input>0:
    for n in range(1,console_input+1):
        formula = n/(n+1)
        result = result + formula
    
    print("Output is:",round(result,2))
        
else:
    print("Please enter an integer >0")



###############################################################################
