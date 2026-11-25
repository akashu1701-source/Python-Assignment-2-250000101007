# Question 40
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Prime numbers between", start, "and", end, ":")
for n in range(max(2, start), end + 1):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        print(n, end=" ")
print()
