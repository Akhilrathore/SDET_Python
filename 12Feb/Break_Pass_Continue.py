#  Break
for i in range(1, 50):
    print(i)
    if i == 5:
        print("out")
        break
#  Pass
for i in range(1, 50):
    if i == 5:
        pass
    else:
        print(i)

#   Continue
for i in range(1, 15):
    if i % 2 == 0:
        print(f"Even number: {i}")
        continue
    print("Odd number: {i}")