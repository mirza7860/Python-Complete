import math

print(math.pi)
print(math.sqrt(16))
print(math.ceil(1.6))
print(math.floor(16.8))

# Casting a string to a number
zipcode = "1000"
zip_value = int(zipcode)
print(type(zip_value))

# # Error if you attempt to cast incorrect data
# zip_value= int("New York")
# print(zip_value)