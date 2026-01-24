N, M, K = map(int, input().split())

heads = list(map(int, input().split()))
bodies = list(map(int, input().split()))


heads.sort()
bodies.sort()

i = 0  
j=0
count = 0 

while i < N and j < M:
    
    if heads[i] <= bodies[j]:

        count += 1
        i += 1
        j += 1
        if count == K:
            break
    
    else:

        j += 1

if count >= K:
    print("Yes")
else:
    print("No")
