# Python Operators

# Symbols used to perform operations on values
# and the variables that hold those values.


# Arithmetic Operators
print(4 + 4)          # Addition
print(8 - 4)          # Subtraction
print(4 * 2)          # Multiplication
print(8 / 6)          # Division
print(8 // 6)         # Floor Division
print(round(24 / 5))  # Round Division
print(24 % 5)         # Modulus
print(2 ** 4)         # Exponentiation

# Assignment Operators
number1 = 32
number1 += 2
print(number1)

number2 = 64
number2 -= 2
print(number2)

number3 = 96
number3 /= 8
print(number3)

number4 = 128
number4 *= 8
print(number4)

# String Concatenation
fname = "First_Name "
lname = "Last_Name"
print(fname + lname)

# Comparison Operators
print(64 == 64)  # Equal to
print(64 == 32)  # Not equal to
print(64 != 64)  # Greater than
print(64 != 32)  # Less than or equal to

# Logical Operators
print(64 < 32)   # Less than
print(64 > 32)   # Greater than
print(64 >= 32)  # Greater than or equal to
print(64 <= 32)  # Less than or equal to

# Logical Operators with Boolean Values
a = True
b = False
c = True

print(not a)       # NOT Operator
print(not b)

print(a and b)     # AND Operator
print(a or b)      # OR Operator
print(b or a)
print(c and b)
print(b and c)


#  if-else statement
num = 32
print('')

if num > 8:
    print("Right on!")
else:
    print("Not today")

#  Ternary operator

temperature = 25

print("It's hot!") if temperature > 30 else print("It's not too hot.")
