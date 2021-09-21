# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:50:45 2021

@author: saqlain
"""

#1.Write a program which will find factors of given number and 
# find whether the factor is even or odd.

def factor(x):
    print("The factors of {} are:".format(x))
    for i in range(1,x+1):
        if (x%i==0):
            if (i%2==0):
                print(i,"is even")
            else:
                print(i,"is odd")
                
factor(50)





#2.Write a code which accepts a sequence of words as input and prints the words
# in a sequence after sorting them alphabetically.

def sorting_words(given_string):
    splitting_words=given_string.split()
    splitting_words.sort()
    
    print('Sorted sequence of words are:')
    
    for word in splitting_words:
        print(word)

sequence_of_words=str(input("enter a sequence of words:"))
sorting_words(sequence_of_words)





#3.Write a program, which will find all the numbers between 1000 and 3000 
#(both included) such that each digit of a number is an even number. 
#The numbers obtained should be printed in a comma separated sequence on a single line.

numbers=[]
for i in range(1000,3001):
    s=str(i)
    if ((int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0)):
        numbers.append(s)
print(",".join(numbers))



#4.Write a program that accepts a sentence and calculate the number of letters 
# and digits.


sentence=input("enter a sentence:")

letter_count=0
digit_count=0


for i in sentence:
    if i.isdigit()==True:
        digit_count+=1
    elif i.isalpha()==True:
        letter_count+=1
    else:
        pass

print("Letter count is:",letter_count)
print("Digit count is:",digit_count)



#5.Design a code which will find the given number is Palindrome number or not.

num = str(input("Enter a number:"))

if (num == num[::-1]):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
