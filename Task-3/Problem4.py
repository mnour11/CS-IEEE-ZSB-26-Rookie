n, t = map(int, input().split())
machines = list(map(int, input().split()))

left = 1
right = min(machines) * t 
answer = right

while left <= right:
    
    mid = (left + right) // 2

    total = 0
    
    for k in machines:
        total += mid // k
        if total >= t:
            break

    
    if total >= t:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
