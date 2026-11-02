name = input("Enter employee name: ")

salary = float(input("Enter monthly salary: "))

tax = salary * 0.10

net_salary = salary - tax

print("----------------------")
print(" SALARY REPORT")
print("----------------------")

print("Employee:", name)
print("Salary:", salary)
print("Tax:", tax)
print("Net Salary:", net_salary)

print("----------------------")