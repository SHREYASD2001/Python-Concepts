# def code(strinss,char):
#     return Strinss.replace(char,'.') 

# strinss=input("Input The String")
# char=input("enter the character whih you want to remove")
# print(code(strinss,char))
# # print(v)

#--------------------------PALINDROME NUMber------------------------------

# s=input("Enter The STring")
# x=s[::-1]
# if s==x:
#     print("palindrome")
# else:
#     print("NOt an Palindrome No.")

#--------------------------check LCM--------------------------------------

#Programme to check whether no are lcm are not.
# a=int(input())
# b=int(input())
# if a>b:
#     lcm=a
# else:
#     lcm=b
# while(1):
#     if(lcm%a==0 and lcm%b==0):
#         print(f"{a} & {b} LCM is {lcm}")
#         break
#     lcm=lcm+1

#-------------------------------------------check HCF/GCD----------------------

# def GCD(a, b):
#     if a == b:
#         return a

#     if a > b:
#         return GCD(a-b, b)
#     else:
#         return GCD(a, b-a)

# def LCM(a, b):
#     return int((a*b)/GCD(a, b))

# print('Enter two numbers")
# a = int(input())
# b = int(input())
# print(f"the HCF of {a},{b} is {LCM(a,b)}")

#-------------------------- HCF/GCD

# a=int(input(""))
# b=int(input(""))
# i=1
# while(a>=i and b>=i):
#     if(a%i==0 and b%i==0):
#         gcd=i
#     i+=1
        
# print(gcd)

#--------------------------------Addition OF FRACTION-----------------------------------------

# a=int(input("numerator of 1st no."))
# b=int(input("denominator of 1st no"))               #sum of fraction
# c=int(input("numerator of 2nd no."))
# d=int(input("denominator of 2nd no"))

# if(b==d):
#     print((a+c)/d)
# else:
#     print(((a*c)+(b*d))/(b*d)) 

#-----------------------------------Count HOw Many Digit----------------------------------------

# x=int(input())
# count=0
# while(x!=0):
#     x=int(x/10)                          count How many digits
#     count+=1
# print(count)

#------------------------------Sum of Digit USing RECURSION------------------------------------------

# def code(c):
    
#     if (c==0):                             #<---------using Recursion sum of digit
#         return 0
#     else:
#          return c%10 +code(int(c/10))
# c=int(input())
# print(code(c))

#---------------------------------------SUM OF N DIGITS-----------------------------------------

# c=int(input())
# print(code(c))
# # sum=0
# # while(c!=0):
# #     sum+=int(c%10)                 <--------- sum of n digit
# #     c=c/10
# # print(sum)

#---------------------------------------SUM OF N DIGITS betwn particular range-----------------------------------------

# def code(c):
#     sum=0
#     for i in range(c+1):                <-------------- sum of n no  of digit
#         sum+=i
#     return sum
# c=int(input("start"))
# x=int(input("end"))
# print(code(c))

#-------------------------------------sum of digit using string-------------------

# sum=0
# n=input()#1111
# for i in n:
#     sum += int(i)
# print(sum)
    

#----------------------------------------SUM OF N DIGITS betwn particular range using range

# def code(c,x):
#     if x==c:
#         return 0
#     else:
#         return x+code(c,x-1)

# print(code(c,x))

#----------------------------------------Factorial using recursion-----------------------------------

# def code(c):
#     if c==0:
#         return 1
#     else:
#         return c*code(c-1)
# c=int(input())
# print(code(c))

#--------------------------------------------Fibonacci Series upto which we want----------------------------------------------

# c=int(input("enter a number upto which you wan the fibonacci series"))
# a=0
# b=1
# if b==0:
#     print(0)
# else:
#     print(0)
#     while(b<c):
#         sum=a+b
#         print(sum)
#         a=b
#         b=sum

#----------------------------------------------check an Leap Year--------------------------

# year=int(input())
# if year%4==0:
#     if year%100!=0:
#         print("Leap year")
#     elif year%400==0:
#         print("Leap Year")
# else:
#     print("Not a Leap YEar")

#---------------------------------------------Prime Number----------------------------------------

# def code(x):
#     i=2
#     while True:
#         if x%i==0:
#             return " THis is not a Prime Number"
#         else:
#             i+=1
#     else:
#         return "This is a Prime Number"
        

# x= int(input())
# print(code(x))

#-----------------------------------------count how many alphabets present are their----------------------------

# x=str(input()) #shreyas

# # y=list(x.split(" "))
# a=[]
# for i in (range(len(x))):
#     if x[i] in a:
#         pass
#     else:
#         a.append(x[i])
#         print(f"{x[i]}={x.count(x[i])}")
    
# print(x)
# print("".join(a))


#------------------------count how many times the given number is present--------------------

# x=int(input())
# for i in range(x):
#     n=input("") #2444
#     b=int(input("counthow many times the given number is present"))
#     #a=[n]
#     print(n.count("4"))
    # for i in range(len(n)):
    #     if n[i]==b:
    #         count+=1
    #     else:
    #         pass


# -----------------------------------------Programm to mix  two string---------------------

# x=input()
# y=input()
# zipped=zip(x,y)
# print(list(zipped))
# sam=[]
# for i in list(zipped):
#     sam.append("".join(i))
# aaa="".join(sam)
# print(aaa)
# if len(x)>len(y):
#     smaller= y
#     bigger  =x
# else:
#     smaller=x
#     bigger = y
# print(sam)
# l = bigger[len(smaller):]
# print(l)
# z=aaa+l

# print(z)

#------------------------------           ADD TWO STRING   -----------------------------------

# name1=input()
# name2=input()
# # a=name1.split()
# # b=name2.split()
# # print(a)
# # print(b)
# for i,j in zip(name1,name2):
#     print(i,j)

#----------------------------------------------REMOVE DUPLICATE digit from the Number----------------------------------

# s=list(map(int,input().strip().split(",")))
# temp=[]
# for i in s:
#     if i in temp:
#         pass
#     else:
#         temp.append(i)
# print(temp)

# #-------------------------------------------get keys in LISt---------------------------

# s=list(map(int,input().strip().split(",")))
# n=list(dict.fromkeys(s))
# print(n)
# a=6

#---------------------------------------------error----------------------------------

# s=list(map(int,input().strip().split(","))) #[1,2,3,5,7,6]
# n=int(input())
# for i in s:
#     if i<n:
#         sums=s[i]+s[i+1]
#         print(sums)

#------------------------------------TAKE AN VALUE FROM USER AND PRINT THE REMAINING VALUE upto 2 decimal places--------------------------------------

# import decimal
# n=int(input())
# x=float(input())
# if n%5==0:
#     b=decimal.Decimal(x-(n+0.5))
#     a=round(b,2)                
#     print(a)
# else:
#     print(x)

# #-----------------------------------------------------------------
# n=input()
# x=n[0]
# y=n[-1]
# a=int(x)+ int(y)
# print(a)


#----------------------------------WAP to dtermine the largest numbe of-------------------------------- 
# x=int(input())
# #z=input()
# for i in range(x):
#     a=list(map(int,input().split(",")))
#     a.sort()
#     # print(a[::-1])
#     print(a[-2])

#-------------------------------------------

# n=int(input())
# for i in range(n):
#     player1,player2=map(int,input().split(",")):
#     if player1>player2:
#         print(player1-player2)     #
#     else:
#         print(player2-player1)    #lag

#-------------------------------find that given string has an palindrome word----------------------------- 

# def code(a):
#     for i in a:
#         if i==i[::-1]:
#             print(f"{i} is an palindrome no.")

#     print(f"{temp} is not an palindrome")
    

# x=input()
# a=x.split(" ")
# print(x)
# code(a)


#---------------------------------WAP to sort the number have an element is present or not

# x=int(input())
# sa=[]
# for i in range(x):
#     a=int(input())            #sort willchange the original list
#     sa.append(a)              #sorted func will not chnage the original list.
# y=sorted(sa)
# print(y)


# n=int(input())
# if n%4==0:
#     print(n+=1)

#--------------------------------fibonacci Srries-------------------------------
# n=int(input())
# a=0
# b=1
# if n==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(n-2):
#         sum=a+b
#         print(sum)
#         a=b
#         b=sum

#---------------------------------Armstroong Number-----------------
# n=int(input()) #153
# temp=n
# sum=0
# for i in str(n):
#     print(i)
#     a=temp%10
#     sum+=(a**len(str(n)))
#     temp=temp//10
# print(sum)
# if sum==n:
#     print("Given Number is an Armstrong NO.")
# else:
#     print("Given number is not an Armstrong Number")
#--------------------------OR---------------------------------------------------
# n=int(input())
# temp=int(n)
# sum=0
# while temp>0:
#     a=temp%10
#     sum+=(a**len(str(n)))
#     temp=temp//10

# print(sum)
# if sum==n:
#     print("Given Number is an Armstrong NO.")
# else:
#     print("Given number is not an Armstrong Number")
    
#-----------------------WAP to check whether the gven number is prime or not-----------

# x=int(input()) #17
# y=int(input()) #21
# count=0
# for j in range(x,y+1):
#     for i in range(2,j):
#         if j%i==0:
#             break
#     else:
#         print(j)
#         count+=1
    
# print(count)

#------------------------WAP to find armstrong no in the interval-------------------------
# x=int(input())
# y=int(input())
# for i in range(x,y+1):
#     temp=i
#     sum=0
#     while temp>0:
#         a=temp%10
#         sum+=(a**len(str(i)))                                   
#         temp=temp//10
#         # print(sum)
#     if sum == i:
#         print(i)
    

# x= lambda a:a**2
# print(x(map(int,input().split(","))))

# --------------------------------shortlist the number dividble by any no.

# n=int(input())
# a=list(map(int,input().split(",")))
# for i in a:
#     if i%n==0:
#         print(i,end=",")

#-------------------------------find the factors of the number------------------------

# n=int(input())
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)              #another way we can append it to the list and then count the
#         count+=1              #particular number how many times partivcular number is there
# print(count)


# #-------------------------Programm TO find Outn The calendar---------------------------
# # Program to display calendar of the given month and year
# # importing calendar module
# import calendar
# yy = 2014 # year
# mm = 11 # month
# # To take month and year input from the user
# # yy = int(input("Enter year: "))
# # mm = int(input("Enter month: "))
# # display the calendar
# print(calendar.month(yy, mm))


# #------------------------------

# import os
# file_stat = os.stat('my_file.txt')
# print(file_stat.st_size)

#------------------------------return the values using commas---------------------------------------------

# def name():
#         return "John","Armin"
# #---------------------------------------------print the tuple with the returned values---------------------------------------------
# print(name())
# #------------------------------------- get the individual items---------------------------------------------
# name_1, name_2 = name()
# print(name_1, name_2)

# #----------------------------------two list into the dict.
# index = [1, 2, 3]
# languages = ['python', 'c', 'c++']             #it's just like add two string question
# dictionary = dict(zip(index, languages))
# print(dictionary)

# #-----------------------WAP TO DETERMINE CLASS NAME
# class Vehicle:
#     def name(self, name):
#         return name
# v = Vehicle()
# print(v.__class__.__name__)

#------&&&&&&&&&&&&&&&&&&&&&*((((*^&*(-Python Program to Split a List Into Evenly Sized-$%^&*%^&__________IMP
# def split(list_a, chunk_size):
#   for i in range(0, len(list_a), chunk_size):
#     yield list_a[i:i + chunk_size]
# chunk_size = 2
# my_list = [1,2,3,4,5,6,7,8,9]
# print(list(split(my_list, chunk_size)))


#=--------------------add two dictionARY
# dict_1 = {1: 'a', 3: 'b'}                
# dict_2 = {2: 'c', 4: 'd'}
# print(dict_1 | dict_2)       #union method

# dict_1 = {1: 'a', 2: 'b'}
# dict_2 = {2: 'c', 4: 'd'}
# print({**dict_1, **dict_2})   #kwargs method

# dict_1 = {1: 'a', 2: 'b'}
# dict_2 = {2: 'c', 4: 'd'}

# dict_3 = dict_2.copy()
# dict_3.update(dict_1)    #update and copy method

# print(dict_3)

#---------------------------set question
# # Program to perform different set operations like in mathematics# define three sets
# E = {0, 2, 4, 6, 8};
# N = {1, 2, 3, 4, 5};

# #set union 
# print("Union of E and N is",E | N)

# # set intersection
# print("Intersection of E and N is",E & N)

# # set difference
# print("Difference of E and N is",E - N)

# # set symmetric difference
# print("Symmetric difference of E and N is",E ^ N)

#------------------------------------------------------Factorial of a number using recursion and normal

# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)
# print(f"{n} factorial of given number is {fact}")

# def code(x):
#     if x==1:
#         return x
#     else:
#         return x*code(x-1)

# x=int(input())
# print(code(x))


#------------------------------------------------Armstrong Number-------------------------------------------------------
# n=input()
# s=0
# for i in n:
#     s+=int(i)**len(n)
# # print(s)
# if s==float(n):
#     print("Armstrong Number")
# else:
#     print("Not a Armstrong Number")

#---------------------------------------------------Odd OR Even No.-----------------------------
# n=int(input())
# if n%2==0:
#     print("Even No.")
# else:
#     print("Odd No.")

# ----------------------------------------------Fibonacci Series----------------------------------
# n=int(input())
# a=0
# b=11:
#     pr
# if n==int(a)
# elif n==2:
#     print(a)
#     print(b)
# else:
#     print(a)
#     print(b)
#     for i in range(n-2):
#         sum=a+b
#         a=b
#         b=sum
#         print(sum)

# ------------------------------------------------Factorial Number-----------------------------------------
# def factj(n):
#     if n<=1:
#         return 1
#     else:
#         return n*factj(n-1)

# n=int(input())
# print(factj(n))

# ---------------------------------------Average of 2 num---------------------------------
# a=int(input())
# b=int(input())
# print((a+b)/2)

# ------------------------------------------gcd or hcf-------------------

# a=int(input())
# b=int(input())
# i=1
# while(a>=i and b>=i):
#     if(a%i==0 and b%i==0):
#         gcd=i
#     i+=1
        
# print(gcd)

# ----------------------------------------------LCM---------------------------------------

# def LCM(a,b):
#     if a>b:
#         lar=a
#     else:
#         lar=b
#     while(1):
#         if (lar % a==0 and lar % b==0):
#             return lar
#         lar = lar + 1

# a=int(input())
# b=int(input())
# print(LCM(a,b))

# ----------------------------------------------swapping two number-----------------------

# a=int(input())
# b=int(input())
# # a=(a+b)-b
# # b=(a+b)-a
# print((a+b)-a)
# print((a+b)-b)

# -------------------------------------------------add two string----------------------------
# a=input()
# b=int(input())
# print(a+"  -  "+str(b))

# --------------------------------------------greatest no in 3-----------------------------------

# a=int(input())
# b=int(input())
# # c=int(input())
# # if a>b and a>c:
# #     print(a)
# # elif b>c:
# #     print(b)
# # else:
# #     print(c)

# # -------------------------------------------------Leap Year---------------------------------

# # n=int(input())
# # if n%4==0:
# #     if n%100!=0:
# #         print("Leap Year")
# #     elif n%400==0:
# #         print("Not a Leap Year")
# #     else:
# #         print("")

# # -----------------------------------------------------prime number---------------------------

# # n=int(input())
# # if n==1:
# #     print("Prime No.")
# # else:
# #     for i in range(2,n):
# #         if n%i==0:
# #             print("Not a Prime number")
# #             break
# #     else:
# #         print("Prime Number")

# # -----------------------------------------------find number between range------------------------
# a=int(input())  #5
# b=int(input())  #9
# for i in range(a,b+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)


# n=int(input())
# new=[]
# for i in range(n):
#     a=[map(int,input().split())]
#     new.append(a)
# aa=[]
# for i in zip(*new):
#     print(tuple([i]))

# print(aa)
# ---------------------------------------------------------USE OF ZIP Function------------------------------------------------
# a=int(input())
# z=[]
# for i in range(a):
#     s=[map(int,input().split())]
#     z.append(s)
# new=[]
# for i in zip(*z):
    
#     new.append(i)
# print(new)




# n=int(input())
# a=[0,1,2,3,4,5,6,7,8,9,10]
# x=[]
# y=[]
# z=[]
# for i in a:
#     if n==i:
#         break
#     else:
#         x.append(i)
# for i in a:
#     if n==i:
#         continue
#     else:
#         y.append(i)
# for i in a:
#     if n==i:
#         pass
#     else:
#         z.append(i)

# print(f"x is {x}")

# print(f"Y is {y}")

# print(f"z is {z}")


# if __name__ == '__main__':
#     n = int(input())
#     arr=list(map(int, input().split()))
#     a=max(arr)
#     arr.remove(a)
#     for i in arr:
#         if a==i:
#             arr.remove(a)
#     print(max(arr))
# if __name__ == '__main__':
    # n = int(input())
    # arr=list(map(int, input().split()))
    # new=list(set(arr))
    # new.sort()
    # print(new[-2])


# if __name__ == '__main__':
#     new=[]
#     new_list=[]
#     for i in range(int(input())):
#         name = input()
#         score = float(input())
#         new.append([name,score])
#         new_list.append(score)
#     a=list(set(new_list))
#     print(a)
#     a.remove(min(a))
#     print(a)
#     for i in new:
#         if min(a)==i[1]:
#             print(i[0])
        
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = []
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks.append([name,scores])
#     query_name = input()
#     new=[]
#     for i in student_marks:
#         if query_name==i[0]:
#             a=sum(scores)
#             print(a/3)
#         else:
#             print("dddd")



# for i in range(int(input())):
#     s=input()
#     a=s.split()
#     print(a.count(4))


# -------------------------------------------------------NA----------------------------------------------------------

# def diagonalDifference(arr):
#     count=0
#     s=0
#     for i in range(len(arr)):
#         count+=int(arr[i][i])
#     for i in range(len(arr)-1,-1):
#         s+=int(arr[i][i])
#     print(count)
#     print(s)
#     return (count+s)
    

# # if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

# n = int(input().strip())

# arr = []

# for _ in range(n):
#     arr.append(list(map(int, input().rstrip().split())))

# result = diagonalDifference(arr)
# print(result)
#     # fptr.write(str(result) + '\n')

#     # fptr.close()








































# --------------------------------------------------------general OOPS programme----------------------------
#  class laptop:
#     def __init__(self,brand,model_name,price):
#         self.brand=brand
#         self.model=model_name
#         self.price=price

#     def give_percentage(self,num):
#         return f"{self.price-((self.price*num)/100)}"
    
# p1=laptop('asus','sonicmaster',30000)
# # num=int(input())
# print(p1.give_percentage(50))