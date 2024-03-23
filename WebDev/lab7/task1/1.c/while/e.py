a = int(input())
cnt = 1
b = 2
while a > b:
    cnt += 1
    b = pow(2,cnt)

print(cnt)