year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Year: ", year, " is a Leap Year")
else:
    print("Year: ", year, " is not a Leap Year")
