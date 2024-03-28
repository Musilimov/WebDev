a = int(input())
cnt = 0
prev = int(input())
current = int(input())
for i in range(2, a):
    d = int(input())
    if(current > prev and current > d):
        cnt += 1
    prev = current
    current = d

print(cnt)
