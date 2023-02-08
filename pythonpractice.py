'''
Created on Jan 28, 2023

@author: somoneletman
'''
from selenium import webdriver

#browser = webdriver.Chrome()
#browser.get('http://selenium.dev/')

#===============================================================================
# name="Somone"
# age = 26
# sal=100000.9898
# Approach
# 
# print("My name is: " ,name)
# print("My age is: " ,age)
# print("My salary is: " ,sal)
# 
# %s is string, %d = integer, %g = decimal
# print("My name is: %s  Age: %d Salary: %g" %(name,age,sal))
# 
# 
# print('Name:{0}  Age:{1}   Salary: {2}'.format(name,age,sal))
# 
# a=30
# 
# if 0:
#     print("This condition is TRUEEEE")
# else:
#     print("This condition is FALLLSEEE")
#===============================================================================
    
    
#===============================================================================
# Even or odd
# a=15
# if a % 2==0:
#     print("Number is EVENNNN")
# else:
#     print("Number is ODDDD")
#===============================================================================
    
    
#===============================================================================
# Multiplication
# if True:
#     print("statement1")
#     print("statement2")
#     print("statement3")
# else:
#     print("statement4")
#     print("statement5")
# print("This is not part of if or else blocks")
#===============================================================================


#===============================================================================
# Single Line
# print("welcome") if 10>20 else print("Python")
# 
# print("welcome") if  10<20 else print("Python")
# 
# elif
# a=20
# if a==10:
#     print("Ten")
# elif a ==20:
#     print("Twenty")
# elif a ==30:
#     print("Thirty")
# else: #Optional
#     print("Not listed")
#===============================================================================
    
    
#===============================================================================
#  range() : values between the range
# 
# print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
# print(list(range(5,10))) # [5, 6, 7, 8, 9]
# 
# print(list (range(1,10,2))) # 1 is starting point, 10 is range, 2 is increment value...1+2 = 3.. 3+2 = 5.. 5+2 = 7, 7+2 = 9
# 
# print(list (range(2,10,2))) # 2 is starting point, 10 is range, 2 is increment value.. 2+2 = 4, 4+2 =6, 6+2 = 8
# 
# print(list (range(10,1,-1))) # 10 is starting point, 1 is range, -1 is decrement value.. [10, 9, 8, 7, 6, 5, 4, 3, 2]
# 
# print(list(range(-10,-5))) #[-10, -9, -8, -7, -6]
# 
# print(list(range(-10, -5, 2))) #[-10, -8, -6]
#===============================================================================


#===============================================================================
# While loop
#
# print 1.....10 numbers
# i=1 #initialization
# while i < 10:
#     print(i)
#     i=i+1
# print("All done!!")
# 
# 
# print 1...10 numbers in descending order
# i=10
# while i >= 1:
#     print(i)
#     i = i -1
# print("All done!!")
#===============================================================================
    
    
#===============================================================================
#   For Loops
#
#   print 1...10  numbers using for loop
# 
# for i in range(1,10):
#     print(i) 
#     
# print only even numbers between 1...20
# for i in range(0,21,2):
#     print(i)
#     
# print only even numbers between 1..20
# for i in range(1,21,2):
#      print(i)
#     
# print 1....10 numbers in descending order
# for i in range(10,0,-1):
#     print(i)
#   
# print 5, 10,15,20...100
# for i in range(5,105,5):
#     print(i)
#   
#  break continue
# 
# skip 5
# for i in range(1,10):
#     if i ==5:
#         continue
#     print(i)
# print("program exited!!!")
# 
# skip 3, 5, 7
# for i in range(1,10):
#     if i ==3 or i==5 or i==7:
#         continue
#     print(i)
# print("program exited!!!")
# 
# 3 is starting, 7 is ending point, 2 is increment
# for i in range(3,7,2):
#     print(i)
#===============================================================================

#===============================================================================
# num1 = 100
# num2=10.5
# print(type(num1))   #int
# print(type(num2))   #float
# 
# find maximum of 3 numbers max()
# max() returns maximum value
# print(max(10,20,30,40,50,5,10,80,100,40)) #100
# 
# min() returns minimum value
# print(min(10,20,30,40,50,5,10,80,100,40)) #5
# 
# print(max(10.5,20.5,)) #20.5
# print(min(10.5,20.5,5.5)) #5.5
#===============================================================================



#===============================================================================
# create string variable
# Example 1: ways of creating string variables
# s = "welcome"
# s = 'welcome'
# s = str('welcome')
# s = str("welcome")
# 
# creating empty string variables
# name = " "
# name = ' '
# name = str( )
#===============================================================================

#===============================================================================
# Example 2 : ways of creating string variables
# mutable - can change the value of the variable
# immutable - cannot change the value of variable
# string is immutable
# if the unique id/value is changed after updating then it is immutable
# 
# str1="welcome"
# print(id(str1)) #4404615216
# str1=str1+"to python" #4404797776
# print(id(str1))
#===============================================================================

#===============================================================================
# Example 3 : + and * with string
# str="welcome"   
# print(str+"programming")     #concatenation/joining = welcomeprogramming
# print(str*3)    #welcomewelcomwelcome
#===============================================================================


#===============================================================================
# Example 4 : slicing
# 
# str="welcome"
# print(str[1:3]) #1 is starting INDEX (INDEX start from 0) 3 is 3rd in range.. = .#el
# print(str[:6]) #did not provide starting index means 0 start by default...0 index is w , 6 is ending value of m = welcom
# print(str[2:]) #did not provide ending index so it will consider all remaining values .. = #lcome
# print(str[1:-1]) #this will remov
#===============================================================================

#===============================================================================
# Example 5 :  ord()  and chr() 
# ord - returns the number representing the unicode code of a specified character
# chr - returns the number representing the unicode code of a specified character.. ex chr(98) returns b
# 
# print(ord('A')) #65 - returns the ASCII code of the character
# print(chr(65))  #A returns character represented by a ASCII number
#===============================================================================

#===============================================================================
# Example 6 : max() min() len()
# print(max("abc"))   #c
# print(min("abc"))   #a
# print(len("welcome"))   #7
#===============================================================================

#===============================================================================
# Example 7: in , not in operators - returns true/false
# s = "welcome"
# print("come" in s) #true
# print("lome" in s) #false
# 
# print("come" not in s) #False
# print("lome" not in s) #True
#===============================================================================


#===============================================================================
# Example 8: String comparison
# print("tim" == "tie") #False
# print("free" != "freedom") #True
# print("arrow" > "aron") #True
# print("right" >= "left") #True
# print("teeth" < "tee") #False
# print("yellow" <= "fellow") #False...y is greater than f
# print("abc" > " ") #True
#===============================================================================

#===============================================================================
# Example 9: Testing strings True/False
# s = "welcomE to python"
# print(s.isalnum()) #Checks if this string contains a number...#False
# print("Welcome".isalpha()) #does string contain only alphabets...#True
# print("2012".isdigit()) #does string contain only digits...True
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
# print("first Number".isidentifier()) #is the string a python identifier #false
# print(s.islower()) #does string contain only lower case... #True
# print("WELCOME".isupper()) #does string contain only upper case...#True
# print("   ".isspace()) #does string contain a space...#True
#===============================================================================

#===============================================================================
# Example 10: Searching for substrings
# s = "welcome to python"
# print(s.endswith("thon")) #True
# print(s.startswith("good")) #false
# print(s.find("come")) #finds which position the given value starts by idex ... = 3
# print(s.find("become"))#-1 =  not found...it is not found
# print(s.count("t")) #2 #Returns number of occurrences of substring the string
#===============================================================================

#===============================================================================
# Example 11: Converting String
# s = "String in PYTHON"
# s1=s.capitalize() #convert all characters to uppercse and turns to string
# print(s1) #String in python #only first character is capitalized because it is only valid for one continuous word
# s2 = s.title() #title() convert whole string to title (each letter capitalized)
# print(s2)
# s3 = s.lower() 
# print(s3) #string in python
# s4 = s.upper()
# print(s4) #STRING IN PYTHON
# s5 = s.swapcase()
# print(s5) #sTRING IN python
# s6 = s.replace("in", "on")
# print(s6)
#===============================================================================

#===============================================================================
# Example 12: Reverse a string
# Method 1
# s="welcome"
# rev_str=" "
# 
# for i in s:
#     rev_str = i+rev_str
# print("reversed string is: ", rev_str) #emoclew
#===============================================================================


#===============================================================================
# Method 2
# s="welcome"
# rev_str=s[::-1] #s[start:end:-1] (starting point not provided = 0 index, end point not provided so all characters considered, -1 means start from end) = #s[0:7:-1]
# print(rev_str)
#===============================================================================


#===============================================================================
# #===============================================================================
# # #===============================================================================
# # # Collections
# # # List - A collection which is ordered and chageable, mutable
# #===============================================================================
# # Example1: how to create list
# # mylist1=[10,20,30,40,50]
# # mylist2=["apple","banana","cherry"]
# # mylist3=["apple",10,"banana",20]
# # mylist=list() #empty list
# # 
# # print(mylist1)
# # print(mylist2)
# # print(mylist3)
# # print(mylist)
# #===============================================================================
# 
# #===============================================================================
# # Example2: Accessing items from the list
# # mylist=["apple","banana","cherry"]
# #===============================================================================
# 
# #===============================================================================
# # print(mylist[0])
# # print(mylist[2])
# # print(mylist[-1])#3 total count in list, index is from 0-2...3-1 = 2..index 2 is cherry
# # print(mylist[-2]) #3 total count in list, index is from 0-2... 3-2 = 1..index 1 is banana
# #===============================================================================
# 
# #===============================================================================
# # Example: 3 Range of indexes
# # mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# # print(mylist[2:5]) #['cherry', 'orange', 'kiwi'] between cherry and melon..start from cherry, 5th is not included because n-1
# # print(mylist[-4:-1]) #['orange', 'kiwi', 'melon'] #7 total count in list, index is from 0-6..7-4 = 3...index 3 = orange-kiwi
# #===============================================================================
# 
# #===============================================================================
# # Example 4: Change item value
# # mylist=["apple","banana","cherry"]
# # print(mylist) #['apple', 'banana', 'cherry']
# # mylist[0] = "orange" #change first element in list to orange
# # print(mylist) #['orange', 'banana', 'cherry']
# #===============================================================================
# 
# #===============================================================================
# # Example5: Read the list items using loop
# # mylist=["apple","banana","cherry"]
# # 
# # for i in mylist:
# #     print(i)
# # 
# # Example 6: Check if the item exists in the list or not
# # mylist=["apple","banana","cherry"] 
# # 
# # if "apple" in mylist: 
# #     print("Yes, apple is present.")
# # else:
# #     print("No, apple is not present.")
# #===============================================================================
# 
# #===============================================================================
# # Example 7: List length (count number of items in a list)
# # mylist=["apple","banana","cherry"]
# # print(len(mylist)) #returns length of list ...3
# # 
# # Example 8: Add items append() - added at end...... insert() - added at specified order
# # mylist=["apple","banana","cherry"]
# # mylist.append("orange") ...added at end
# # print(mylist) #["apple","banana","cherry","orange"]
# # 
# # mylist.insert(1, "orange") #....added at index 1
# # print(mylist) #['apple', 'orange', 'banana', 'cherry']
# #===============================================================================
# 
# 
# #===============================================================================
# # Example9: Remove item from the list pop() or del()
# # pop()
# # mylist=["apple","banana","cherry"]
# # mylist.pop(0) 
# # print(mylist)  #['banana', 'cherry']
# #  
# # del()
# # del mylist[2]   #del command removes single item based on the index
# # print(mylist)   #['apple', 'banana']
# #  
# # clear() - removes all items from list
# # mylist=["apple","banana","cherry"]
# # mylist.clear()
# # print(mylist)
# #===============================================================================
# 
# #===============================================================================
# # #Example10: Copy one List into another
# # #list()
# # #mylist1=["apple","banana","cherry"]
# # #mylist2=list(mylist1)   #copy mylist1 into mylist2
# # #print(mylist1)  #['apple', 'banana', 'cherry']
# # #print(mylist2)  #['apple', 'banana', 'cherry']
# # 
# # copy()
# # mylist1=["apple","banana","cherry"]
# # mylist2=mylist1.copy()   #copy mylist1 into mylist2
# # print(mylist1)  #['apple', 'banana', 'cherry']
# # print(mylist2)  #['apple', 'banana', 'cherry']
# #===============================================================================
# 
# 
# #===============================================================================
# # #Example 11: Combine/Join lists
# # #1 Approach: Using  + operator
# # #list1 =["a","b","c"]
# # #list2 =[1,2,3]
# # #list3=list1+list2
# # #print(list3) #['a', 'b', 'c', 1, 2, 3]
# #  
# # #2. Approach: Using loop statement
# # #list1=["a","b","c"]
# # #list2 =[1,2,3]
# #   
# # #for i in list2:
# #  #   list1.append(i)
# # #print(list1)    #['a', 'b', 'c', 1, 2, 3]
# # 
# # 3. Approach: Using extend() function
# # list1=["a","b","c"]
# # list2 =[1,2,3]
# # list1.extend(list2)
# # print(list1)    #['a', 'b', 'c', 1, 2, 3]
# #===============================================================================
# 
# 
# #===============================================================================
# # #Example 12: Compare two lists
# # 
# # mylist1=(10,20,30)
# # mylist2=('a', 'b','c')
# # 
# # if tmylist1 == mylist2:
# #     print("Lists are twins")
# # else:
# #     print("Lists aren't twins)    
# #===============================================================================
#===============================================================================


#===============================================================================
#===============================================================================
# # Collections
# # Tuple - a collection which is ordered and unchangeable, immutable
#===============================================================================
# 
#===============================================================================
# # Example 1: Creating tuble
# # mytuple =("apple, banana, cherry")
# # print(mytuple)  #apple, banana, cherry
#===============================================================================
# 
#===============================================================================
# # Example 2: Access tuple items
# # mytuple=("apple", "banana", "cherry")
# # print(mytuple[1])   #banana here index starts from -
# # 
# # print(mytuple[-1])  #cherry
#===============================================================================
# 
# 
#===============================================================================
# # Example 3: Range of indexes
# # mytuple=("apple", "banana", "cherry", "orange","kiwi","melon", "mango")
# # print(mytuple[2:5]) #('cherry', 'orange', 'kiwi')
# # print(mytuple[-4:-1])   #('orange', 'kiwi', 'melon
#===============================================================================
# 
# 
#===============================================================================
# # Example 4: Changing tuple items
# # We CAN'T..Why? - tuples are immutable. If it is immutable:
# # 1. We cannot modify existing Value
# # 2. We cannot append new value
# # 3. We cannot insert a new value
# # 4. We cannot remove a value
# # Work Around.. Change tuple into a list object and then modify from there., then convert back. tuple--> list(modify) --> tuple
# # 
# # mytuple=("apple", "banana", "777") #1.declare tuple
# # mylist = list(mytuple)      #2.create a list with the contents of your tuple
# # mylist[0]= ["orange"]       #3. modify your list..in this case, changing the item orange to 0 index value 
# # mytuple=tuple(mylist)     #4. Add the modified contents of list to your tuple
# # print(mytuple)                  #(['orange'], 'banana', '777')
#===============================================================================
# 
# 
#===============================================================================
# # Example 5: Reading tuple items using loop
# # mytuple=("apple", "banana", "cherry")
# # for i in mytuple:
# #     print(i)
#===============================================================================
#     
#===============================================================================
# # Example 6: Check if Item Exists (searching for item in tuple)
# # if "banana" in mytuple:
# #     print("We found the banana.")
# # else: 
# #     print("Cannot find banana.")
#===============================================================================
# 
#===============================================================================
# # Example 7: Tuple length - counting items in a tupel
# # mytuple=("apple", "banana", "cherry")
# # print(len(mytuple))     #3
#===============================================================================
# 
#===============================================================================
# # Example 8: Add items to tuple
# # WE CANNOT, Tuples are Immutable, only possible through changing tuple to list
# # mytuple=("apple", "banana", "cherry")
# # mytuple[0] = "orange"
# # print(mytuple)      #TypeError: 'tuple' object does not support item assignment
#===============================================================================
# 
#===============================================================================
# # Example 9: Copy tuple - we can do this because we are not directly changing any of the tuple data
# # mytuple1=("apple", "banana", "cherry")
# # mytuple2 =mytuple1
# # print(mytuple2) #('apple', 'banana', 'cherry')
#===============================================================================
# 
#===============================================================================
# # Example 10: Remove items from tuple..CANNOT..tuples are immutable
# # mytuple=("apple", "banana", "cherry")
# # mytuple.remove()        #AttributeError: 'tuple' object has no attribute 'remove'
# # 
# # del mytuple         #cannont, tuple = immutable
#===============================================================================
# 
#===============================================================================
# # Example 11: Join/combine tuple
# # tuple1=(10,20,30)
# # tuple2=('a', 'b','c')
# # 
# # tuple3 = tuple1+tuple2
# # print(tuple3)       #(10, 20, 30, 'a', 'b', 'c')
#===============================================================================
# 
# 
#===============================================================================
# # Example 12: Compare two tuples
# # tuple1=(10,20,30)
# # tuple2=('a', 'b','c')
# # 
# # if tuple1 == tuple2:
# #     print("Tuples are twins")
# # else:
# #     print("Tuples aren't twins")    
#===============================================================================
#===============================================================================



#Collections
#Set

#Collections
#Dictionary