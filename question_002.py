# Question 2
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
if b == 0:
    print("Divisor cannot be zero")
else:
    print("Floor division (a // b):", a // b)
    print("Modulus (a % b):", a % b)
