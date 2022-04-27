n = int(input())
suma = 0
while n > 0:
    b = n % 10
    suma += b
    n = n // 10
print("Сумма цифр числа =", suma)