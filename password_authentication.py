correct_pin = "1234"
attempts = 3

while attempts > 0:
    entered_pin = input(f"رمز عبور را وارد کن ({attempts}): ")

    if entered_pin == correct_pin:
        print("خوش آمدید! دسترسی تأیید شد.")
        break

    else:
        attempts -= 1
        print("رمز اشتباه است.")