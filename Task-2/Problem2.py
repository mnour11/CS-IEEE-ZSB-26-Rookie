import sys
data = sys.stdin.read().split()
it = iter(data)

t = int(next(it))
out = []

for _ in range(t):
    n = int(next(it))
    q = int(next(it))
    arr = [0] + [int(next(it)) for _ in range(n)]

    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i-1] + arr[i]

    total = pre[n]

    for _ in range(q):
        l = int(next(it))
        r = int(next(it))
        k = int(next(it))

        s = pre[r] - pre[l-1]
        length = r - l + 1
        new_sum = total - s + length * k

        if new_sum % 2 == 1:
            out.append("YES")
        else:
            out.append("NO")

print("\n".join(out))
