def factorial(num):
    if num > 0:
        flag = 1
        for i in range(1, num + 1):
            flag *= i
        return flag
    else:
        print("Invalid input")
        return 0


no = int(input("number for Factorial: "))
result = factorial(no)
print(result)
