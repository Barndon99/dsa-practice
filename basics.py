#input grabs user input
name = input("What is your name? ")

print("Hello, " + name + "!")

# 3 types of data types
# 1. Strings
# 2. Integers
# 3. Booleans

float = 2.1
num = 2

print(float + num) # prints 4.1


# Python has full access to built in methods
string = "Hello World"

# This returns a new string it doesn't modify the original
print(string.upper()) # prints "HELLO WORLD"
print(string) # prints "Hello World"
print(string.find("World")) # prints 6

# Of course we can use comparison operators
print(1 == 1) # prints True

# Boolean expressions (or and not)
print(1 == 1 and 2 == 2) # prints True
print(1 > 2 or 2 < 3) # prints True
print(1 != 1) # prints False

# If statements
temperature = 24
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = int(weight) * 0.45
    print("You are " + str(converted) + " kilos")
else:
    converted = int(weight) / 0.45
    print("You are " + str(converted) + " pounds")

# While loops
i = 1
while i <= 5:
    print(i)
    i += 1

# Lists (arrays)
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names[0]) # prints John

# List methods
names.append("Jenny") # adds Jenny to the end of the list
names.insert(0, "Anthony") # adds Anthony to the beginning of the list
names.remove("Bob") # removes Bob from the list

print(names) # prints ['Anthony', 'John', 'Mosh', 'Sarah', 'Mary', 'Jenny']

# For loops
for name in names:
    print(name)

# Range function
# Ranges generate a list of numbers
numbers = range(5)

for number in numbers:
    print(number) # prints 0, 1, 2, 3, 4

# Tuples (immutable lists)
numbers = (1, 2, 3)
#number[0] = 10 # This will throw an error









