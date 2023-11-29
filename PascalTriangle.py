# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import factorial
print("====================== Hello! Welcome to Pascal Triangle generator ===========")
print("1. Press P for Printing triangle ")
print("2. Press T for Time Complexity ")
press = input("Enter :: ")
if press == 'P' or press == 'p':
    print("Press your desire method to print pascal triangle")
    print("1. Simple python code")
    print("2. Using powers of 11")
    print("3. Using Bionomial of Cofficient")
    print("4. Using factorial ")
    print("5. Exit")
    user = int(input("Enter your choice :: "))
    # taking number of rows
    n = int (input ("Enter the number of rows for pascal triangle: "))
    # checking condition of user

    # python code for pascal triangle
    if user == 1:
        
        # list for storing numbers
        li = [[] for i in range(n)]
        for i in range (n):
            for j in range(i+1):
                
                # less than index i
                if(j < i):
                    
                    # for index zero
                    if(j == 0):
                        li[i].append(1)
                        
                    # adding previous iteration values
                    else:
                        li[i].append(li[i-1][j]+li[i-1][j-1])
                        
                # for same index i and j
                elif(j == i):
                    li[i].append(1)
                    
        # printing the triangle
        for i in range(n):
            # adjust space
            print(' '*(n-i), end='')
            
            for j in range(i+1):
                # print the column
                print(" " ,li[i][j], end="")
                
            print()
            
    # power of 11 for pascal triangle      
    elif user == 2:
        
        for i in range(n):
            a = 11**i
            # adjust space
            print(' '*(n-i), end='')
            
            # compute power of 11
            print(' '.join(map(str,str(a))))
            
    elif user == 3:
        
        for i in range(1, n+1):
            for j in range(0, n-i+1):
                
                print("",end=" ")
     
        # first element is always 1
            C = 1
            for j in range(1, i+1):
     
            # first value in a line is always 1
                print(C, end=' ')
     
            # using Binomial Coefficient
                C = C * (i - j) // j
            
            print()   
            
    elif user == 4:
        for i in range(n):
            for j in range(n-i+1):
     
            # for left spacing
                print(end=" ")
     
            for j in range(i+1):
     
            # nCr = n!/((n-r)!*r!)
                print(factorial(i)//(factorial(j)*factorial(i-j)), end="  ")
     
        # for new line
            print(" ")
            
    # exit
    else:
        print("Exit")
        
        
if press == 'T' or press == 't':
    print("Time Complexity of pascal triangle from different methods :: ")
    print()
    print()
  
    print("Time Complexity by Using method power of 11 :: O(N)")
    
    print("Time Complexity by Using Binomial Coefficient :: O(N^2)")
    
    print("Time Complexity by Using factorial :: O(N^2)")

            
print('===================================================================')
    
