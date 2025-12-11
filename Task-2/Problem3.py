import sys
data = sys.stdin.read().strip().split()
it = iter(data)

N = int(next(it))
Q = int(next(it))

p1 = [0] * (N + 1)
p2 = [0] * (N + 1)
p3 = [0] * (N + 1)

for i in range(1, N + 1):
    v = int(next(it))
    p1[i] = p1[i-1] + (1 if v == 1 else 0)
    p2[i] = p2[i-1] + (1 if v == 2 else 0)
    p3[i] = p3[i-1] + (1 if v == 3 else 0)

out = []

for _ in range(Q):
    a = int(next(it))
    b = int(next(it))
    out.append(str(p1[b] - p1[a-1]) + " " +
               str(p2[b] - p2[a-1]) + " " +
               str(p3[b] - p3[a-1]))

sys.stdout.write("\n".join(out))
