n = int(input())
b = 0
while n != 0:
    a = n % 10
    if a == 5:
       b += 1
    n //= 10
print("В числе", b, "5ки")