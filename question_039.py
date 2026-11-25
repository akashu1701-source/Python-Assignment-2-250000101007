# Question 39
n = int(input("Enter a number: "))
if n < 2:
    print(n, "is not prime")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    print(n, "is prime" if is_prime else "is not prime")
