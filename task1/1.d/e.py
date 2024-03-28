a = int(input())
prev = int(input())
found = False
for i in range(1,a):
    b = int(input())
    if((prev >= 0 and b >= 0) or ((prev < 0 and b < 0))):
        found = True
    prev = b

if(found):
    print("YES")
else:
    print("NO")