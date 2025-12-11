import sys
data = sys.stdin.read().split()
it = iter(data)

n = int(next(it))
arr = [0] + [int(next(it)) for _ in range(n)]

pre1 = [0] * (n + 1)
for i in range(1, n + 1):
    pre1[i] = pre1[i-1] + arr[i]

sorted_arr = sorted(arr[1:])
pre2 = [0] * (n + 1)
for i in range(1, n + 1):
    pre2[i] = pre2[i-1] + sorted_arr[i-1]

m = int(next(it))
out = []

for _ in range(m):
    t = int(next(it))
    l = int(next(it))
    r = int(next(it))
    if t == 1:
        out.append(str(pre1[r] - pre1[l-1]))
    else:
        out.append(str(pre2[r] - pre2[l-1]))

print("\n".join(out))
