def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))
