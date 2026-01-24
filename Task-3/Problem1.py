n, k = map(int, input().split())

left = 1
right = n
answer = n

while left <= right:
    mid = (left + right) // 2


    total = 0
    temp = mid
    while temp > 0:
       
        total += temp
        temp //= k

   
    if total >= n:
       
        ans = mid
        right = mid - 1
   
    else:
        left = mid + 1

print(ans)
