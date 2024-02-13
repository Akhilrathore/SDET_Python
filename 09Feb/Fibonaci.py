num = int(input("Enter Number: "))
a,x = 0,0
b, y= 1,1
print(a, ",", b, end="")
for i in range(2, num):
    c = a + b
    a = b
    b = c
    print(", ", c, end="")
# ------------------
print ("\nwithout 3rd variable")
for i in range(2, num):
    x = y
    y = x + y

    print(", ", b, end="")
