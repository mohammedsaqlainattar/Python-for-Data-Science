# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 00:30:02 2021

@author: saqla
"""

import os
import csv

file = open(os.path.join(r"C:\Users\saqla\Desktop\Python Certification for Data Science\Modules\Module 3\Dataset","bank-data.csv"),"r")

csv_reader = csv.DictReader(file)


unique_jobs = set()
age = []
max_min_age = {}

print(csv_reader.fieldnames[0],csv_reader.fieldnames[1])
for line in csv_reader:
    
    print(line['age'],line['job'])
    unique_jobs.add(line['job'])
    age.append(line['age'])
    max_min_age.update(max_age=int(max(age)),min_age=int(min(age)))
  
while True:    
    profession = input("Enter profession:").casefold()

    if profession in unique_jobs:
        print(profession,"is eligible for loan")
    
    elif profession == "end":
        break

    else:
        print(profession,"is not an eligible profession for loan! \nPlease enter valid profession")
        

