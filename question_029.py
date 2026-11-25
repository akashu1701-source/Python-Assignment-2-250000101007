# Question 29
n = int(input("Enter a number: "))
if n % 5 == 0 and n % 11 == 0:
    print(n, "is divisible by both 5 and 11")
elif n % 5 == 0:
    print(n, "is divisible by 5 only")
elif n % 11 == 0:
    print(n, "is divisible by 11 only")
else:
    print(n, "is divisible by neither 5 nor 11")
