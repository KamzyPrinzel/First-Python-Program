# Variable Section
student_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print (student_count)

# String Section
course_name = "Python Programming"
print(len(course_name)) #Used to get the length of a string
print(course_name [0]) # Used to fetch the index or a particular character in a string 
print(course_name [-1]) # Used to fetch the first character from the end of the string
print(course_name [0:3]) # Used to fetch the first three indexes of the string
print(course_name [0:]) # used to fetch from the first index to the end of the string 

course = "Python \"Programming" # \ is an escape character used to exclude the character after it 
print (course) 

name = "My \n Program" # is used to push the succeeding string to the next line

# Concantenation
first = "Prince"
last = "Abiaziem"
full = first + " " + last
print(full)

# Formatted String
first_name = "Abiaziem"
last_name = "Abiaziem"
full_name = f"{first_name} {last_name}"
print (full_name)

# String Methods: These methods are the functions or things that an object is capable of doing. It is captured with the "." noatation
print(course.upper()) # converts the string to upper case
print(course.title()) # capitalizes each word
print(course.lower()) # converts the string to lower case 
print(course.find("Pro")) # Used to get the index of a string 
print(course.replace("P", "j")) # Replaces P with P
print("Pro" in course) # Returns a boolean output. It is used to check if a character or characters is present in a string
print ("Swift" not in course) # Returns a boolean value. It is used to check if a character(s) is not present in a string

# Numbers 
x = 1 #  Integers
y = 1.1 # Float
z = 1 + 2j # Complex numbers

# Basic Operations
print (10 + 3 ) # Addition
print (10 - 3 ) # Subtraction
print (10 * 3 ) # Multiplication
print (10 / 3 ) # Division that returns a float value
print (10 // 3 ) # Division that returns an integer value 
print (10 % 3 ) # modulo
print (10 ** 3 ) # exponential. (10^3)

# Augumented value
a = 12
a = a + 2
a += 2
print(a)

#Working with Numbers
import math

print(round (2.9)) # Rounding up a number
print (abs(-2.9)) # Fethcing the absolute value of a number 

print(math.ceil(2.2)) # fetching the ceiling of a number 

# Type Conversion
b = input("Enter your age: ")
c = int(b) + 1
print(f"Enter your age: {b}, New age: {c}")
