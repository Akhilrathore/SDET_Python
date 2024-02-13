str1 = input("Enter string: ")
str2 = ""
n = len(str1) - 1
for i in range(len(str1)):
    str2 = str2 + str1[n - i]
if str2 == str1:
    print({str1}, " is a palindrome")
else:
    print({str1}, " is not a palindrome")
#     ------------------------------------------------
flag = True
for i in range(len(str1) // 2):
    if str1[i] != str1[len(str1) - i - 1]:
        flag = False
        break
if flag:
    print({str1}, " is a palindrome")
else:
    print({str1}, " is not a palindrome")

# ----------------------
if str1 == str1[::-1]:
    print({str1}, " is a palindrome")
else:
    print({str1}, " is not a palindrome")
