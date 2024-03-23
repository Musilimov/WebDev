def is_power_of_two(n):
    return n != 0 and (n & (n - 1)) == 0

N = int(input())

if is_power_of_two(N):
    print("YES")
else:
    print("NO")
