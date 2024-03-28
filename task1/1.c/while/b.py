a = int(input())
b = 2
while a > 0:
    if(a % b == 0):
        break
    else:
        b += 1

print(b)
