import sys
input = sys.stdin.readline

n, q = map(int, input().split())
x = list(map(int, input().split()))


pref = [0] * (n + 1)
for i in range(1, n + 1):
    pref[i] = pref[i - 1] ^ x[i - 1]


for _ in range(q):
    a, b = map(int, input().split())
    print(pref[b] ^ pref[a - 1])
