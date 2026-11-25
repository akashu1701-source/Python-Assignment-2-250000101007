# Question 48
# else runs only if the loop completes without break
for i in range(1, 6):
    print(i)
else:
    print("for loop completed normally (no break)")

for i in range(1, 6):
    if i == 3:
        print("break at 3")
        break
else:
    print("This will NOT be printed because of break")
