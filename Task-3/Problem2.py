n = int(input())
prices = list(map(int, input().split()))


prices.sort()

q = int(input())

for _ in range(q):
    m = int(input())

    left = 0
    right = n - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if prices[mid] <= m:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    print(ans + 1)
