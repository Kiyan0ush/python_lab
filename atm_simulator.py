balance = 1_000_000

while True:

    print("\n----- ATM MENU -----")
    print("1. مشاهده موجودی")
    print("2. برداشت وجه")
    print("3. واریز وجه")
    print("4. خروج")

    choice = input("انتخاب کن: ")

    if choice == "1":
        print("موجودی شما:", balance)

    elif choice == "2":
        amount = int(input("مبلغ برداشت: "))

        if amount <= balance and amount > 0:
            balance -= amount
            print("برداشت موفق بود.")
            print("موجودی جدید:", balance)

        else:
            print("موجودی کافی نیست یا مبلغ نامعتبر است.")

    elif choice == "3":
        amount = int(input("مبلغ واریز: "))

        if amount > 0:
            balance += amount
            print("واریز موفق بود.")
            print("موجودی جدید:", balance)

        else:
            print("مبلغ نامعتبر است.")

    elif choice == "4":
        print("از همراهی شما سپاسگزاریم.")
        break

    else:
        print("گزینه نامعتبر است.")