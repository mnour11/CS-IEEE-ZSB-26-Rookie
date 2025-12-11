import sys
data = sys.stdin.read().split()
it = iter(data)

n = int(next(it))
k = int(next(it))
q = int(next(it))

MAX = 200000
diff = [0] * (MAX + 3)

for _ in range(n):
    l = int(next(it))
    r = int(next(it))
    diff[l] += 1
    diff[r + 1] -= 1

cover = [0] * (MAX + 2)
for i in range(1, MAX + 1):
    cover[i] = cover[i-1] + diff[i]

good = [0] * (MAX + 2)
for i in range(1, MAX + 1):
    good[i] = good[i-1] + (1 if cover[i] >= k else 0)

out = []
for _ in range(q):
    a = int(next(it))
    b = int(next(it))
    out.append(str(good[b] - good[a-1]))

print("\n".join(out))
