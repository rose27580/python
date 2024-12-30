# Factorial calculation
n = int(input("Enter the number for factorial calculation: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(n, "! =", fact)

# Fibonacci series calculation
n = int(input("Enter the number for Fibonacci series calculation: "))
a, b = 0, 1
print("FIBONACCI SERIES:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()  # for a new line after the series

# Sum of elements in a list
a = [34, 56, 78, 98, 56]
print("Sum is:", sum(a))
