user_tier = input("سطح کاربری (Gold/Silver/Normal): ")
purchase_amount = float(input("مبلغ خرید: "))

if user_tier == "Gold" or purchase_amount > 1_000_000:

    if user_tier == "Gold":
        discount = 0.20

    else:
        discount = 0.15

elif user_tier == "Silver":
    discount = 0.10

else:
    discount = 0.05

print("Discount:", discount * 100, "%")