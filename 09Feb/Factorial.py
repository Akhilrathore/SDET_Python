num = int(input("Enter Number: "))
tmp = 1
if num >0:
    for i in range(1, num+1):
        # print (i)
        tmp *= i
    print("Factorial of ", num, " is: ", tmp)
else:
    print("incorrect input")

