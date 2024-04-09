n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.reverse()
for i in a:
    print(i, end=" ")
