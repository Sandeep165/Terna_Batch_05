# Python Datatype
'''
Text Type:      	str
Numeric Types:	    int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type:	    dict
Set Types:      	set, frozenset
Boolean Type:	    bool
Binary Types:	    bytes, bytearray, memoryview
'''

#String Datatype
#   I have 4 children's
'''
Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are

'''
str1 = "I have 4 children's"

# str2 = 'I have 4 children's'

str3 = '''Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are'''

# print(str1)
# print(str2)
# print(str3)

# take inp user the age name and city.....print thhe name age city f tring
# take 3 nums user display sum for first two no....display multiplication of last two no....display subs of first and last no
# addition of 5 and 4 is 9

line = "I love Python."
print(len(line))   #ans-1

#string Slicing
#var_name[start:end:step]

# print(line[0]) #I
# print(line[7]) #P
# print(line[13]) #P


para = "take 3 nums user display sum for first two no....display multiplication of last two no....display subs of first and last no take inp user the age name and city.....print thhe name age city f strinG"
 #40-1 = 39
# print(para[len(para)-1])


# str4 = "Hello world"
# print(len(str4)) #11-1 = 10

line = "I lOve Python 78 "
# string Slicing
# var_name[start:end:step]

# print(line[2:6])   #love
# print(line[2:7])   #love
# print(line[7:13])   #Python
# print(line[2:13])   #love Python
# print(line[:])   #love Python
# print(line[-2]) 


#String methods
print(line)
# print(line.upper())
# print(line.lower())
# print(line.capitalize())
# print(line.isdigit()) #false
# print(line.isalpha())
print(line.count("o"))


'''

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

'''
# age = int(input("enter age:"))
# name = input("enter name:")
# city = input("enter city:")
# print(f"{name} {age} {city}")



num1=int(input("enter 1st num: "))
num2=int(input("enter 2nd num: "))
num3=int(input("enter 3rd num: "))

print(f"sum of {num1} and {num2} is {num1+num2} mul of {num2} and {num3} is {num2*num3} sub of {num1} and {num3} is {num1-num3} ")

'''
if else
for loop
list set tuple

'''