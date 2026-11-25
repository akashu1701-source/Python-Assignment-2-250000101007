# Question 10
n = int(input("Enter a two-digit number: "))
n = abs(n)
if 10 <= n <= 99:
    print("Sum of digits:", n // 10 + n % 10)
else:
    print("Not a two-digit number")
