t = int(input())


for _ in range(t):
   
    n = int(input())
    w = list(map(int, input().split()))

    l, r = 0, n - 1
    sumL = sumR = 0
    best = 0

   
    while l <= r:
        
        if sumL < sumR:
            sumL += w[l]
            l += 1
        
        elif sumR < sumL:
            sumR += w[r]
            r -= 1
       
        else:
       
  
            best = max(best, l + (n - r - 1))
            sumL += w[l]
            l += 1

    print(best)
