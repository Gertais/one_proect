a = int(input("Введите число: "))
if a % 100 >= 10 and a % 100 < 20 or a % 10 > 4 or a % 10 == 0:
    print(a, "рублей")
elif a % 10 == 1:
    print(a, "рубль")
else:
    print(a, "рубля")
