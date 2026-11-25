# Question 49
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("while loop completed normally (condition became False)")

i = 1
while i <= 5:
    if i == 3:
        print("break at 3")
        break
    i += 1
else:
    print("This will NOT be printed because of break")
