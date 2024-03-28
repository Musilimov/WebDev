a = int(input())
b = 0
for i in range(2,a+1):
    if(a % i == 0):
        b = i
        break

print(b)