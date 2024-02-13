import math

print("Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take "
      "pie as 3.14)")
r = float(input("Enter Circle radius: "))
print("Circle area: ", math.pi * (pow(r, 2)), "(using import - math)")

print("Create a program that takes two numbers as input and prints whether the first number is greater than, "
      "less than, or equal to the second number.")
x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))

result = "First number is greater" if x > y else "Second number is greater"
# result = x if x > y else y
print(result)


print("Develop a Python script that calculates the square and cube of a given number.")
n = int(input("Enter a number for  square and cube: "))
print("Square: ", n ** 2)
print("Cube: ", n ** 3)
