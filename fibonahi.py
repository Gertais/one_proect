n = int(input("Введите число, для нахождения последовательности Фибоначчи: "))
a = 0
b = 1 
if n > 1:
    for i in range(1, n):
        a, b = b, a + b
        print(b)
elif n == 1 or n == -1:
    print(1)
elif n == 0:
    print(0)
elif n < 1:
    for i in range(-1, -n):
        b, a = a, b - a
        print(b)