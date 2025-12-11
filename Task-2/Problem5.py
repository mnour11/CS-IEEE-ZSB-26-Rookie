from math import gcd
import sys
input = sys.stdin.read

data = list(map(int, input().split()))
N = data[0]
A = data[1:]

prefix_gcd = [0] * (N+2)
suffix_gcd = [0] * (N+2)

for i in range(1, N+1):
    prefix_gcd[i] = gcd(prefix_gcd[i-1], A[i-1])

for i in range(N, 0, -1):
    suffix_gcd[i] = gcd(suffix_gcd[i+1], A[i-1])

max_gcd = 0
for i in range(1, N+1):
    current_gcd = gcd(prefix_gcd[i-1], suffix_gcd[i+1])
    max_gcd = max(max_gcd, current_gcd)

print(max_gcd)
