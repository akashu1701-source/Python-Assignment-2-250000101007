# Question 19
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b:", a is b)
print("a is c:", a is c)
print("a == c:", a == c)
print("a is not c:", a is not c)
x = None
print("x is None:", x is None)
print("id(a), id(b), id(c):", id(a), id(b), id(c))
