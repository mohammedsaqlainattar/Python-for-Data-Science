#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os


# In[ ]:


df = pd.read_csv(os.path.join(r"C:\Users\saqla\Desktop\Python Certification for Data Science\Modules\Module 3\Dataset","FairDealCustomerData.csv"),header=None)

df.rename(columns={0:'lname',1:'fname',2:'blacklist'},inplace=True)

df['fullname'] = df['fname'] + df['lname']

df.drop(columns = ['lname','fname'],inplace =True)

faircust = (df['blacklist'] == 0)
faircustlist = list(df.loc[faircust,'fullname'])
blockcustlist = list(df.loc[~faircust,'fullname'])

class customer:
    customers = []
    def __init__(self,custlst):
        self.custlst = custlst
    def __del__(self):
        self.customers =[]
    def IsFair(self,name):
        if name in self.custlst:
            print('{0} is a fair customer'.format(name))
        else:
            raise Exception


try:
    fr = customer(faircustlist)
    fr.IsFair(input('Enter Customer Name for an Order:'))
#     print(fr.customers)

except:
    print('Sorry!!Input Customer is a blacklisted.')


# In[ ]:




