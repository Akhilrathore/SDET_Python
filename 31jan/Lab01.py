print('Syntax Error:')
# Explain the difference between the = operator and the == operator in Python.
a = 10
print(a)

b = 3
# '=' is use for assignment value

print("Compare a, b:", a == b)

c = 4
# What does the ** operator do in Python, and how is it used?
print("Power:", a ** c)

# What does the ^ operator do in Python, and in what context is it commonly used?
print(a ^ b)
"""If both bits are 0 or both bits are 1, the result is 0.
If one bit is 0 and the other bit is 1, the result is 1.
"""
a = 5  # 101 in binary
b = 3  # 011 in binary

result = a ^ b  # Perform XOR operation

print(result)  # Output: 6   (110 in binary)

# Use of ^ : Encryption: XOR is a fundamental operation in many encryption algorithms.

print(~1)

# Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take pie as 3.14)
r = float(input("Enter Circle radius: "))
print("Circle area: ", r ** 2 * 3.14)

# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))

if x > y:
    print("First number is greater")
elif x < y:
    print("Second number is greater")
else:
    print("Both number are equal")

# Develop a Python script that calculates the square and cube of a given number.
n = int(input("Enter a number for  square and cube: "))
print("Square: ", n ** 2)
print("Cube: ", n ** 3)
