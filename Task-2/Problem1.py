
import sys

data = sys.stdin.read().strip().split()
it = iter(data)
n = int(next(it)); q = int(next(it))
arr = [int(next(it)) for _ in range(n)]

pref = [0]*(n+1)
for i in range(1, n+1):
    pref[i] = pref[i-1] + arr[i-1]

out = []
for _ in range(q):
    a = int(next(it)); b = int(next(it))
    out.append(str(pref[b] - pref[a-1]))
sys.stdout.write("\n".join(out))
