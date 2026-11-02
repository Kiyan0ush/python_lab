for i in range(1, 51):

    if i % 3 == 0:
        continue

    if i % 5 == 0:
        continue

    if i == 42:
        break

    print(i)