import sys
input = sys.stdin.readline

N = int(input())
a = [int(input()) for _ in range(N)]

T = 0
for v in a:
    T ^= v

x = [T ^ v for v in a]
print(*x)
