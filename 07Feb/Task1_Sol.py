print('syntax error:')

print("\nQues #1: Explain the difference between the = operator and the == operator in Python.")
print("Ans #1: > ")
a = 9
b = 3
print("'=' is use for assignment value. a = ", a)

print("'==' is Compare operator, ", end="")
print("Compare a == b:", a == b)

c = 4
print("\nQues #2: What does the ** operator do in Python, and how is it used?")
print("Ans #2: > ")
print("'**' Operator do power, eg. a = ", a, ", c = ", c, ", a ** c: ", a ** c)

print("\nQues #3: What does the ^ operator do in Python, and in what context is it commonly used?")
print("'^' = ")

"""
If both bits are 0 or both bits are 1, the result is 0.
If one bit is 0 and the other bit is 1, the result is 1.
"""
a = 5  # 101 in binary
b = 3  # 011 in binary

result = a ^ b  # Perform XOR operation
print("a = ",a,", binary of a is: ",bin(a))
print("b = ",b,", binary of b is: ",bin(b))
print(" a ^ b = : ",result)  # Output: 6   (110 in binary)
print("Use of ^ : Encryption: XOR is a fundamental operation in many encryption algorithms.")

print(~1)
