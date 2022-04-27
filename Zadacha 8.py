n = int(input())
five = False
while n != 0:
    b = n % 10
    if b == 5:
        five = True
    n = n // 10
if five == True:
    print("Цифра 5 есть в числе",)
else:
    print("Цифры 5 нет в числе")
