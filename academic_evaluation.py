gpa = float(input("معدل: "))
units = int(input("تعداد واحد: "))

if gpa >= 17:
    print("وضعیت: ممتاز")

elif gpa >= 10:
    print("وضعیت: عادی")

else:
    print("وضعیت: مشروط")