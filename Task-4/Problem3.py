from collections import defaultdict

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    total = defaultdict(int)
    for x in a:
        total[x] += 1

    limit = {}
    
    for v in total:
        limit[v] = total[v] // k

    
    cnt = defaultdict(int)
    l = 0
    ans = 0

    for r in range(n):
       
        cnt[a[r]] += 1

       
        while cnt[a[r]] > limit[a[r]]:
          
            cnt[a[l]] -= 1
            l += 1

        ans += r - l + 1

    print(ans)
