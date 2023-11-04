# ---------------------str---------------------------
# a = 'NaVeEn,1,2.0'                 #strnig ,int, float,
# print(a)
# a="NaVeEn"                         # for convert lower case
# b=a.lower()
# print(b)
# print(a.lower())
# b=a.upper()                        # for convert upeer case
# print(b)
# print(a[::-1])                     # for reverse str
# a='apple','banana','apple','mango','apple' # count particuller elements
# print(a.count('apple'))
# a=[1,2,3,4,5,6,7,8,9,10]
# print(sum(a))                    # sum of list
# --------list-------------------
# a=['naveen',1,2,3,1.0,2.0]         # list can modified
# print(a)
# print(a[0])                        # to get item
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(len(a))                      # to get length
# to get any 2to 5 char
# print(a[2:5])
# a[1]='vikas'                       # apend
# print(a)
# a=input('enter the name:')         # take input from user
# print(a)
# a='Naveen'
# print(len(a))                      # length
# for i in a:                        # itrate str from loop
#   print(i)
# print(a.endswith('n'))             # true
# print(a.startswith('N'))           # false
# print(a.count('e'))                # count prticuler aliments
# a='naveen kumar'
# print(a.capitalize())              # capital first latter
# print(a.find('e'))                 # find the word indexing in str
# print(a.find('v'))
# print(a.replace('naveen', 'navin' )) # replace word

# ----------------------list-----------------mutable----------------------
# a=['naveen','kumar','vikas']      # reverse list
# a.reverse()
# print(a)
# a.append('singh')                 # apend elements
# print(a)
# a.remove('kumar')                 # remove  elements
# print(a)
# a=['naveen','kumar',1,2,3,4,5,]   # list indexing
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# a.append("singh")                 # apend new elements in list
# print(a)
# a.remove(4)                       # remove  elements
# print(a)
# a.clear()                         # clr list all elements
# print(a)
# b=['singh',9,8,7,6]
# a.extend(b)                       # extends list
# print(a)
# a = ['naveen', 'kumar', 1, 2, 3, 4, 5, ]
# a.insert(2, 'singh')
# print(a)
# a.pop(1)                          # delete particuller items from index
# print(a)
# a.remove(2)                       # remove particuller item from name
# print(a)
# a.reverse()                       # list reverse
# print(a)
# a.sort()                          # only work with str upper case sort to first index
# print(a)
# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))   # remove duplicatte from list
# print(mylist)
# a=[1,2,3,4,1,3,5,4]
# b=list(dict.fromkeys(a))
# print(*set(a))
# print(b)                #  remove duplecte make set
# ----------------------dict-----------------------------
# dict={                            # get value from dict
#  'naveen':'singh',
#  'amit':'kumar',
#  'ravi': 'rana' }
# print(dict['naveen'])
# --------------------------------------------------
# dict={}                           # take unput from user create dict
# a= int(input('enter the elements :'))
# for i in range(a):
#      b= input('enter the key :')
#      c= input('enter the value :')
#      dict.update({b:c})
#      print(dict)
# --------------------------------------------
# a = (input('enter the key :'))
# dict={
#     '100':"naveen",
#     '101':"sonu",
#     '102':"ravi",
#     '103':"sumit",
#     '104':'amit'}
# print(dict)         # simple print dict
# print(dict[a])
# dict['100'] = 'kumar'            # for chanage elements
# print(dict)
# dict['107']='singh'  # for add new elements
# print(dict)
# dict.update({'105':'kumar'})     # for update  elements
# print(dict)
# dict.pop('104')                  # for delte any elements
# print(dict)
# for dict in dict.items():        # use loop in dict
#      print(dict)
# child1 = {                       # nested dict
#     "name": "Email",
#     "year": 2004}
# child2 = {
#                 "name": "Tobias",
#                 "year": 2007}
# child3 = {
#                         "name": "Linus",
#                         "year": 2011}
# myfamily = {
#                                   "child1": child1,
#                                   "child2": child2,
#                                    "child3": child3}
# print(myfamily)
# dict = {
#         '100':"naveen",
#         '101':"sonu",
#         '102':"ravi",
#         '103':"sumit",
#         '104':'amit'
#     }
# a=dict.keys()                     # get keys only
# b=dict.values()                   # get value only
# print(a)
# print(b)
# -------------tuple-------immutable----------
# tup=(1,0,3,2,5,6,7,8,9,10,1,2,3,2,1,2,4,5,6)
# a=tup.count(2)                   # count perticuler elements
# print(a)
# a = tup.__len__()                  # to get len of tup
# print(a)
# a=tup.index(0)                   # for indexing
# print(a)
# print(sum(tup))                     # sum of tuple
# ----------sets--------unorderd------
# a={'naveen','kumar','singh'}
# a.add('vikas')                   # for adding  a new elements
# print(a)
# a.remove('naveen')               # for remove a elements
# print(a)
# a = {'naveen', 'kumar', 'singh'}
# b = {"google", "microsoft", "apple"}
# a.update(b)                      # for update 2 or more sets and combind
# print(a)
# --------------------LOOPS----------------------------
# while loop
# a=0
# while a<10:
#     print('hello naveen')
#     a=a+1
# ------------------------------------------
# a=0
# while True:                   # infinite loop
#     print('naveen')
#     a=a+1 
# ------------for loop---------------------------
# for loop
# for i in range(0,100):              # range fun
#     print(i)
# ------------------------------------
# a='Naveen'
# for i in a:
#     if i=='e':
#         break                        # break stmt
#     print(i)
# ----------------------------------------------
# a='Naveenkumar'
# for i in a:
#     if i=="n":
#         continue                     # continue stmnt
#     print (i)
# # ------------------------------------------------------
# def find_max(nums):
#     max_num = float("-inf")      # smaller than all other numbers
#     for num in nums:
#         if num > max_num:
#          max_num=num
#     return max_num
# a = print("Hello", end=' ')
# print(a)
# ---------file methods-----------------------------
# import webbrowser
# webbrowser.open_new('chini.pdf')  # open pdf
# a = open('naveen.txt', 'r')      # read  or close file
# print(a.read())
# a.close()
# a=open('naveen.txt','r')
# print(a.fileno())                #file no
# a=open('naveen.txt','a')
# a.write('i m writing another line in my file')  # write in file
# a.flush()                                       # flush the data in file
# a=open('naveen.txt','r')
# print(a.isatty())                # return type bool vale
# a=open('naveen.txt','r')
# print(a.readable())              # if file readble return true  else false
# print(a.readline())              # read first line of file
# print(a.readlines())             # return as a list of file
# print(a.seek(4))                 # change file position
# print(a.seekable())              # true if seekable else false
# a.readline()
# print(a.tell())                  # current file postion after reading first line
# a.truncate                       # resize the file
# a=open('naveen.txt','a')
# print(a.writable())              # true if writable else false
# a.writelines(['this is my new line '])  # write line in list \n for new line

# li=['a','b','c']
#                  #.join keywords
# print('d'.join(li))
# import os
# os.remove('naveen.txt')          # for remove file
# os.rmdir('foldername')           # delete folder
# ---------------numpy--------------------------------------------
# import numpy         # numpy is a python librarary working with arrys
# a=numpy.array([1,2,3,4,5,6,7,8,9,10 ]) # 1-D array
# print(a)
# print(type(a))                     # type of array
# a=numpy.array((1,2,3,4,5,6,7,8,9,10)) # use a tupple to cerate array
# print(a)
# a=numpy.array([[1,2,3,4,5], [6,7,8,9,10]])  # 2-D array
# print(a)
# print(a.ndim)                      # typee of 2-D array
# a=numpy.array([[[1,2,3],[4,5,6],[7,8,9]]]) # 3-D arrays
# print(a)
# print(a.ndim)
# a=numpy.array([1,2,3,4,5], ndmin=5 # to make dimensional array
# print(a)
# a=numpy.array([1,2,3,4,5])
# print(a[0])                         # acceess arrray elements
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[::-1])                      # reverse array
# a=numpy.array([[1,2,3,],[4,5,6]])   # acceess 2-D array elemenst
# print(a[1,0])
# a=numpy.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
# print(a[0,1,2])                     # access 3-D array elemets
# a=numpy.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(a[1,-2])                      # negative indexing
# a=numpy.array([1,2,3,4,5,6,7,8,9,10])
# print(a[0:5:])    # start:step:end  # slicing array
# print(a[1:])
# print(a[::9])
# a=numpy.array([1,2,3,4,5,6,7])      # negative slicing array
# print(a[-5:-1])
# a=numpy.array([[1,2,3,4],[5,6,7,8]])
# print(a[0:2,1:3])                   # access 2-D array
# ------------------Data type in numpy-------------------------------
# i - integer                         # numpy has some extra data type
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type(void)
# import numpy
# a=numpy.array([1,2,3,4,5])                    # int
# b=numpy.array(['aAa','bBb','cCc','dDd'])
# print(a.dtype)
# print(b.dtype)
#-------------local and global var--------
# a=2             
# def add():
#     b=3       
#     c=a+b
#     print(c)
# add()
#------------------------------------------
# def add():
#     a=2        # local var
#     c=a+b
#     print(c)
# b=3            # global var
# add()
#----------add two numbers--------------------------------
# def add(x,y):
#     sum=x+y
#     return sum
# print(add(5,2))
#-------adding three numbers by fun ----------------------
# def add (a,b,c):
#     sum=a+b+c
#     print(sum)
# add(2,1,5)
#----------------lambda -----------------------------------
# x=lambda a: a+10
# print(x(5))
# x=lambda a: a*10
# print(x(5))
# x=lambda a,b:a-b
# print(x(2,3))
#-------------lambda fun ------------------------------------------
# def myfunc(n):
#       return lambda a : a * n
# mytripler = myfunc(3)
# print(mytripler(11))
#---------------------------------------------------
# def fun(a):
#     return lambda b: b*a
# c=fun(2)
# print(c(3))       # output 6
#-------------------------------------------------
# a=[1,2,5,4,7,8,11,22,9]         # using filter in lambda 
# b=filter(lambda x :x>4,a)
# print(list(b))
#------------------------------------------------------------
# a=['a','a','b','b','c','c',1 ,1,2,3,2,3]
# a=list(dict.fromkeys(a))  # remove duplicate by fromkeys
# print(a
# a = [1, 2, 3, 4, 4, 2, 1, 4, 3, 5, 6]
# b = []
# [b.append(x) for x in a if x not in b] # remove duplicate by append and for loop
# print(b)
# print(list(set(a)))     # remove duplicate making a set#
# def fun (x):              # remove duplicate by function
#     return list(dict.fromkeys(x))
# b=fun([1, 2, 3, 4, 4, 2, 1, 4, 3, 5, 6]) 
# print(b)
#----------------remove duplicate------------------------------------------
# a = [1, 2, 3, 4, 4, 2, 1, 4, 3, 5, 6]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
#----------------remove  duplicate -----------------------------------
# def fun(x):
#     return list(set(x))
#-----------remove duplicate-------------------
# a = [1, 2, 3, 4, 4, 2, 1, 4, 3, 5, 6]
# print(a)
# print(set(a))

#-------------------------------------

#---------------------------------------------------------
# a = [1, 2, 3, 4, 4, 2, 1, 4, 3, 5, 6]
# print(set(a))          # to create set remove  duplicate
# print(list(set(a)))     # to create list remove duplicate
#-------------------------------------------------
# a=[1,2,3,4,5,7,80,10,20,40,0,30]     # sequence of list
# a.sort()
# print(a)
# print(a[-1])
# print(max(a))           # to find a max elements
# print(min(a))           # to finde a min elemets
#-------------------------------------------------
# a=['naveen','kumar','choudhary']        # get len of elements
# print('this is the results of a')
# print(len(a))
# for i in a:
#     print(len(i))   
#---------------find the large elements------------------
# a='naveen','kumar','chaudhary','kaushambiup'
# for i in a:
# #     print(len(i))
#     b=max(a,key=len)
#     print(b)
#--------------list ---------------
#a = ['naveen', 'kumar', 'chaudhary', 'kaushambiup']
# b = max(a, key=len)
# c=min(a,key=len)
# print(b)
# print(c)
# print(len(a))
# a = ['naveen', 'kumar', 'chaudhary', 'kaushambiup']
# print(*a)   # print simple as given
# b=print(a[0])  # slicing of list
# for i in a:
#    b=print(len(i))
# print(min(a,key=len))
# print(max(a,key=len))
#----------------------------------------------
# a = ['naveen', 'kumar', 'chaudhary', 'kaushambiup']
# x=[]
# print(a)
# print(*a, sep=' ')    # using seprator
# for i in a:
#        b=(len(i))
#        x.append(i)   # to get 1st,2nd,3rd elements
#        print(x)
#---------------------------------------------

#-----------for get the len  of tuple --------------------
# a=('naveen','kumar','amit','chaudhary')
# size=0
# for i in a:
#        size+=1
# print(size)
# print(len(a)) # by len fun
#--------------get output in list -------------------------
# a = ('naveen', 'kumar', 'amit', 'chaudhary')
# for i in a:
#        x=len(i)
#        print(x,end=' ')
#------------------------------------------------------
# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")
#     print("\n")
#--------------piramid--------------------
# a=int(input('enter the number:'))

# for i in range(a):
#        for j in range(i+1):
#               print('*',end=' ')
#        print("\n")
#----------------------------------------------------
# a=3
# for i in range(a):                 # 1
#        for j in range(i+1):        # 1 2
#               print(j+1,end=' ')   # 1 2 3
#        print('\n')
#---------reverse piramid------------------------------------
# a=5
# for i in range(a,0,-1):
#        for j in range(1, i+1):
#               print(' *',end=' ')
#        print('\n')
#--------------reverse digit piramid---------------------------------
# a=5
# for i in range(a,0,-1):
#        for j in range(1,i+1):
#               print(j,end=' ')
#        print('\n')
#------------------floyed triangle-----------------------------------
# a=5
# num=1
# for i in range(1,a+1):
#        for j in range(1,i+1):
#               print(num, end=' ')
#               num+=1
#        print()
# a=['naveen','kumar','chaudhary']
# print(a)
# print(*a)
# a.append('ram')
# print(a)
# print(a[0])          # slicing of list
# for i in a:
#        x=len(i)
#        z=print(x,end=' ')
#        print(list)

       
       
#--------------convert name to a letters list-------------------------
# a=[]
# for i in 'Naveen':
#        a.append(i)
# print(a)
#---------------------------------------------------------------------
# a=['naveen','kumar','chaudhary']
# a.reverse()
# print(a)
# for i in reversed(a):
#        print(i)
#-------------------------------------------
# a=[1,2,3,4,5,6,7,8,9,10]
# print(sum(a))
# print(a[0])
# a.reverse()
# print(a)
# print(len(a))
# print(max(a))
# print(min(a))
#----------------------------------------------------
# for i in range(10, 15, 1):
#     print(i, end=' ,')
#-----------------------------------------------
# l1=[x**3 for x in range(4)]
# l1=[l1.pop()+2]
# print(l1)
#---------------------------------------------
# a=[1,2,3,4,5,6]
# b=a.pop(2)
# print(a)
# print(b)
# a.append(10)
# print(a)
# a.remove(4)
# print(a)
#---------------------------------------------
# a = ['naveen', 'kumar', 'chaudhary']
# print(tuple(a))
#-------------------------
# Python3 code to demonstrate
# the working of uniform()
# import random
# print(random.randint(0,9)) # for int crate random number 

# a = 4
# b = 9
# print("The random number generated between 4 and 9 is : ", end="")
# print(random.uniform(a, b))  # for create random float num
# print()
# print(random.random(5)) # for random number
#-----------crate random number with for loop-----------------
# a=[]
# for i in range(0,5):
#     x=random.randint(1, 20)
#     a.append(x)
# print(a)
#---------------sum by range fun----------------------------
# a=range(102)
# print(sum(a))
#---------------------
# n=int(input('enter the elements of ava:'))
# l=[]
# for i in range(1,n+1):
#     x=int(input('enter the number'))
#     l.append(x)
#     y=sum(l)/n
#     print(y)
#-----------reverse number ----------------------
# n=int(input('enter the number for reverse:'))
# b=0
# while(n>0):
#     c=n%10
#     b=b*10+c
#     n=n//10
# print(b)
#--------Dictionary different from List comprehensions----------------
# a=[i for i in range(5)]     # list
# print(a)
# dict={i:i+2 for i  in range(10)} # dict
# print(dict)
#--------take input creat dict from user---------------------
# dict={}
# x=int(input('enter the number of elements:'))
# for i in range(x):
#     a=input('enter the key:')
#     b=input('enter the value:')
#     dict.update({a:b})
# print(dict)
#---------take input for get key--------------
# x=input('enter the key:')
# dict={'1':'naveen',
#         '2':'kumar',
#             '3':'chaudhary'}
# print(dict[x])
#---------creat list from user input-----------------------
# a=[]
# b=int(input('enter the number of element:'))
# for i in range(0,10):
#     ele=int(input('enter the nmber:'))
#     a.append(ele)
# print(a)
#----------join two list--------------------------------------

# l1 = ['x', 'y', 'z']
# l2=['a','b','c']
# for i in (l2):          # with for loop
#     l1.append(i)
# print(l1)
# l3=l1+l2              # list concadination
# print(l3)
# l1.extend(l2)           # list extend
# print(l1)
#--------to get key or value of dict-------------------------
# dict = {
#         '100':"naveen",
#         '101':"sonu",
#         '102':"ravi",
#         '103':"sumit",
#         '104':'amit'
#     }
# print(dict.keys())
# print(dict.values())
# -----------remove-Whitespace-------------------------------
# a='   n a v e e n, kumar, singh  '
# print(a)
# b=a.lstrip()
# print(b)
#----------------------------------------------------------------
# a='1,2,3,4,5,6,7,8,9,10'
# print(a)
# print(list(a))
# print(tuple(a))
# --------------fibonacci series---------------------------
# term=int(input('enter the terms:'))
# n1=0
# n2=1
# count=0
# while count<term:
#     print(n1,end=' ')
#     nth=n1+n2
#     n1=n2
#     n2=nth
#     count+=1
#--------------check given number is prime or not---------------------
# n=int(input('enter the number:'))
# if n>1:
#     #print('2 is prime number' ) 
#     for i  in range(2,int(n/2)+1):
#         if (n%i)==0:
#             print(n,' is not a prime number')
#             break
#     else:
#         print(n,'is a prime number ')
# else:
#     print(n,'is not a prime number')
# -----------------removes vowels from a string-----------------------------------
# name='naveen chaudhary'
# result=''
# vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# for char in  name:
#     if char not in vow:
#         result= result+char 
# print(result)
#--------------check sequence is palindrome or not---------------
# seq = 'malayalam'
# rev=seq[::-1]
# if rev==seq:
#     print('given seq id palindrome:')
# else:
#     print('given seq is not palindrome:')














