import math
a = int(input())
b = 1
while a > b:
    if(math.isqrt(b) ** 2 == b):
        print(b, end=" ")
    b += 1