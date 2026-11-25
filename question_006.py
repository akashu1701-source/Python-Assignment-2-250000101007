# Question 6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if b == 0:
    print("Cannot divide by zero")
else:
    print("a / b  (true division, float):", a / b)
    print("a // b (floor division):", a // b)
    print("Example with negatives: -7 / 2 =", -7 / 2, "and -7 // 2 =", -7 // 2)
