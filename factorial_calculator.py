number = int(input("یک عدد وارد کن: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial:", factorial)