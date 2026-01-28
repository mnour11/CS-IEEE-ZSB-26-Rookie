n = int(input())
t = list(map(int, input().split()))

l, r = 0, n - 1
timeA = timeB = 0
cntA = cntB = 0


while l <= r:
    
    if timeA <= timeB:
        timeA += t[l]
        l += 1
        cntA += 1
   
    else:
        timeB += t[r]
        r -= 1
        cntB += 1

print(cntA, cntB)
