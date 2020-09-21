a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))
c = int(input("Введите целое число c: "))

if a > b:
    if a > c:
        print(f"Max: {a}")
    else:
        print(f"Max: {c}")
else:
    if b > c:
        print(f"Max: {b}")
    else:
        print(f"Max: {c}")


print(f"Max number: {m}")