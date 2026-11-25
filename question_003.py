# Question 3
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
if b == 0:
    print("Divisor cannot be zero")
else:
    remainder = a - (a // b) * b
    print("Remainder:", remainder)
