n, x = map(int, input().split())
a = list(map(int, input().split()))

l = 0
current_sum = 0
count = 0


for r in range(n):
    current_sum += a[r]

   
    while current_sum > x:
        current_sum -= a[l]
        l += 1

    if current_sum == x:
        count += 1

print(count)
