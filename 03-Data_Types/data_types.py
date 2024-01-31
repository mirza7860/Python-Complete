# String data type

# literal assignment

first = "First_Name"
last = "Last_Name"

print(type(first))
print(type(first) == str)
print(type(last))
print(type(last) == str)

print(isinstance(first, str))
print(isinstance(last, str))

# constructor function

pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatenation

fullName = first + " " + last
print(fullName)


fullName += "!"
print(fullName)

# Casting a number to a string

decade = str(1980)
print(type(decade))
print(decade)

# Single line

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple line

multilineStatement = '''
Hello there,

I hope this message finds you well.
I think you are enjoying the github repo .
I wanted to share some exciting news with you.

Stay positive and keep smiling!

Best regards,
Mirza Sahil
'''
print(multilineStatement)

# Escaping special characters

sentence = "I\'m back!\tHey!\n\nWhere\'s this at\\located"
print(sentence)

# String methods
name = "mirzasahil"

print(name)
print(name.lower())
print(name.upper())

multiplelineString = '''
Coding is like solving
        puzzles; 
        each line of 
                  code brings
        the picture 
together!
Whats your take on it !
'''

print(multiplelineString.title())
print(multiplelineString.replace("line", "statement"))
print(multiplelineString)

print(len(multiplelineString))

multiplelineString += "                                        "
multiplelineString = "                    " + multiplelineString

print(len(multiplelineString))

print(len(multiplelineString.strip()))
print(len(multiplelineString.lstrip()))
print(len(multiplelineString.rstrip()))


#  Task
#  Build A Menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffe".ljust(16, ".")+"$2".rjust(4))
print("Cake".ljust(16, ".")+"$8".rjust(4))
print("Ice-cream".ljust(16, ".")+"$4".rjust(4))
print("Cheese".ljust(16, ".")+"$2".rjust(4))

# string index values
cars = "Audi"
print(cars[1])
print(cars[-1])
print(cars[1:-1])
print(cars[1:])

# Some methods rturn boolean vlaues

print(cars.startswith("A"))
print(cars.endswith("i"))

# Boolean data type
myValue = True
d = bool(False)
print(type(d))
print(isinstance(myValue, bool))


#  Numeric data types

#   Integer type
price = 100
print(price)
best_price = int(80)
print(best_price)
print(type(price))
print(isinstance(best_price, int))

#    Float type
gpa = 2.56
y = float(1.14)
print(type(gpa))

# Complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#  Built-in functins for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
