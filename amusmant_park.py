age = int(input("سن: "))

has_permission = input("اجازه والدین (y/n)? ") == "y"

if age >= 18 or (age >= 15 and has_permission):
    print("مجاز به ورود هستید")

else:
    print("اجازه ورود ندارید")