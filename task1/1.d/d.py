a = int(input())
cnt = 0
prev = int(input())

for i in range(1, a):
    d = int(input())
    if d > prev:
        cnt += 1
    prev = d

print(cnt)
