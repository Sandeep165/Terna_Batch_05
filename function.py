# # function--->  code of block....it will run only when we call the function

# # def func_name(): -------------> function defination
# #     statements
# #     statements  --------------> body of a function
# #     statements
# #     statements
# # func_name()  -----------------> calling the function

# # def my_function(): #------------> function defination
# #     print("Hello world!! ") #----------->body of a function

# # my_function()


# # def say_hello():
# #     print("Hello everyone!!")

# # say_hello()


# # parameter and arguments
# # parameters are the variable name that you will be passing inside the func defination
# # arguments are the variable name that you will be passing inside the func call


# def my_function(fname, lname):
#     #print("my first name is", fname,"my last name is", lname)
#     print(f"my first name is {fname} and my last name is {lname}")
#     # print(f"statements....{var_value}")


# my_function("John", "aney")

# # my first name is john and last name is aney


# # def biodata(fname,lname,age):
# #     print(f"my first name is {fname} and my last name is {lname}. My age is{age}")

# # biodata('Alex','Roy',21)


# # def add(num1,num2):
# #     print(num1, "+", num2, "=", num1+num2)
# # add(5,8)

# def operation(num1, num2):
#     num3 = num1 + num2
#     print(num3)
#     num4 = num1 - num2
#     print(num4)
#     num5 = num1 * num2
#     print(num5)
#     num6 = num1 / num2
#     print(num6)


# operation(num1=6, num2=3)


# def my_fun(child3, child2, child1):
#     print("the youngest child is", child3)


# my_fun("emie", "john", "sami")


# my_name = "sam"  # assign the value
# Your_name = "rish"  # compare the value
# if my_name == Your_name:
#     print("true")
# else:
#     print("false")


# def hello(country="India"):
#     print("My country is ", country)  # ..............> india


# hello()
# hello("Sweden")
# hello("usa")


# # (4,5,6)
# # max no is 6

# def max(num1, num2, num3):

#     if num1 > num2 and num1 > num3:
#         print("num1 is largest number", num1)
#     elif num2 > num3 and num2 > num1:
#         print("num2 is largest", num2)
#     else:
#         print("num3 is largest", num3)


# max(5, 78, 9)

# # DRY -----> DO NOT REPEAT YOURSELF


# # print -------> function will print the statement
# # return ------>  return the value to the func

# def say():
#     print("hello world")


# say()
# '''
# Sometimes, we do not know in advance the number of arguments that will be passed into a function. Python allows us to
# handle this kind of situation through function calls with an arbitrary number of arguments.
# In the function definition, we use an asterisk (*) before the parameter name to denote this kind of argument. 
# Here is an example
# '''


# def greet(*names):
#     """This function greets all
#     the person in the names tuple."""

#     # names is a tuple with arguments
#     for name in names:
#         print("Hello", name)


# greet("Monica", "Luke", "Steve", "John")

def numss(*num):
    for i in num:
        print(i)
    print("len is", len(num))
numss(1,2,3,8,2,83,5)