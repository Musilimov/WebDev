def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6
a = int(input())
b = []
for i in range(a):
    c = int(input())
    b.append(c)

print(first_last6(b))