n = int(input())
mult = 1
while n > 1:
    b = n % 10
    mult *= b
    n = n // 10
print("Произведение цифр числа =", mult)