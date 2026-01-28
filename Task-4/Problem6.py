n, x = map(int, input().split())
a = list(map(int, input().split()))

pos = {}
found = False

for i in range(n):
    needed = x - a[i]
   
    if needed in pos:
        print(pos[needed] + 1, i + 1) 
        found = True
        break
    
    pos[a[i]] = i


if not found:
    print("IMPOSSIBLE")
