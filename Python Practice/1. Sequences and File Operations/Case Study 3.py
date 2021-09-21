# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:59:16 2021

@author: saqlain
"""

from cryptography.fernet import Fernet


reference_id = str(input("Enter Reference ID: "))

digit=0
alphabet=0
sp_char=0

if (len(reference_id)==12):
    for i in reference_id:
        if i.isdigit():
            digit+=1
        
        elif i.isalpha():
            alphabet+=1
        
        elif i in list(('$','@','#')):
            sp_char+=1

if (digit>=1 and alphabet>=1 and sp_char>=1 and (digit+alphabet+sp_char)==len(reference_id)):
    print("Reference ID is valid!\n")
    
    generate_key = Fernet.generate_key()
    
    key = Fernet(generate_key)
    
    encrypt_ref_id = key.encrypt(reference_id.encode())
    
    print("The original Reference ID is: ",reference_id)
    print("\nThe Encrypted Reference ID is: ",encrypt_ref_id)

    decode_input = int(input("Do you want to decrypt Reference ID? (Answer: 1->YES,2->NO):"))
    
    if decode_input==1:
        
        decrypt_ref_id = key.decrypt(encrypt_ref_id).decode()
        
        print("\nThe Decrypted Reference ID is: ",decrypt_ref_id)
        print("Program Finished!")
        
    elif decode_input==2:
        print("Program Finished!")
        
    
else:
    print("Reference ID is invalid, Please enter correct Reference ID!")
    
