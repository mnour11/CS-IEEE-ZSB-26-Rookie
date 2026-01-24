n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))

j = 0
ans = 0

for i in range(n):

    while j + 1 < m and abs(cities[i] - towers[j + 1]) <= abs(cities[i] - towers[j]):
        j += 1


    ans = max(ans, abs(cities[i] - towers[j]))

print(ans)
