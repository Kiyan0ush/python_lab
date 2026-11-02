salary = float(input("حقوق ماهانه: "))
has_child = input("آیا فرزند دارید؟ (y/n): ") == "y"

if salary <= 10_000_000:
    tax = 0

elif salary <= 25_000_000:
    tax = (salary - 10_000_000) * 0.10

else:
    tax = (15_000_000 * 0.10) + \
          ((salary - 25_000_000) * 0.20)

if has_child:
    tax -= 500_000

print("----------------------")
print("حقوق:", salary)
print("مالیات:", tax)
print("حقوق پس از مالیات:", salary - tax)