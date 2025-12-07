n = int(input().strip())
nums = list(map(int, input().split()))

if n == 0:
    print(0)
else:
    nums.sort()
    distinct_count = 1 
    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            distinct_count += 1

    print(distinct_count)