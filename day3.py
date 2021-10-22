# conditions-------->if elif else

#age<18------>you are under age
#age>18-45------>you are allowed to drive
#age >45----->You are allowed to seat back

# age = int(input("Enter your age:- "))

# if age<18:
#     print("You are under age!")
# elif age>18 and age<45:
#     print("You are allowed to drive")
# else:
#     print("You are allowed to seat back")
    
'''

a==b:
a!=b:
'''


'''
if (condition)True/False:
    print(body1)
elif (condition)True/False:
    print(body2)
else:
    print(body3)
'''


# Take values of length and breadth of a rectangle from user and check if it is square or not.
# Take two int values from user and print greatest among them.
# <,>,==,!=

# len = int(input("enter the length:- "))
# breadth = int(input("enter the breadth:- "))

# if (len==breadth):
#     print("It is a square")
# else:
#     print("It's not a square")

# num1 = int(input("Enter a numb:- "))
# num2 = int(input("Enter a numb:- "))
# if num1>num2:
#     print("num1 is greater")
# else:
#     print("num2 is greater")

'''

A school has following rules for grading system:
a. Below 25 - F   #if
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B   #elif
f. Above 80 - A   #else
Ask user to enter marks and print the corresponding grade.

'''

# age = int(input("Enter your age:- "))

# if age<18:
#     print("You are under age!")
# elif age>18 and age<45:
#     print("You are allowed to drive")
# else:
#     print("You are allowed to seat back")

marks=int(input("Enter your marks :"))

if(marks<25): 
    print("F")
elif(marks>=25 and marks<45):
    print("E")
elif(marks>=45 and marks<50):
    print("D")
elif(marks>=50 and marks<60):
    print("C")
elif(marks>=60 and marks<80):
    print("B")
else:
    print("A")



'''
Q1 :-
Write a program to print absolute vlaue of a number entered by user. E.g.-
INPUT: 1        OUTPUT: 1
INPUT: -1        OUTPUT: 1

-5  =  5

num*-1  = 1
num*-1  = 8
num*-1  = 100

Q2:-
take 3 num
display the greates one

'''