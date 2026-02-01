n = int(input())
p = list(map(int, input().split()))

total_sum = sum(p)
ans = float('inf')


for mask in range(1 << n):
    s = 0
    for i in range(n):
        if mask & (1 << i):
            s += p[i]
    diff = abs(total_sum - 2 * s)
    ans = min(ans, diff)

print(ans)
