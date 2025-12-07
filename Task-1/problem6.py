
n = int(input().strip())
arr = list(map(int, input().split()))

stack = []  
result = []

for i in range(n):

    while stack and stack[-1][0] >= arr[i]:
        stack.pop()
    

    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][1])  # Index of nearest smaller
    

    stack.append((arr[i], i + 1))

print(*result)