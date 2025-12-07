
n = int(input().strip())

total = n * (n + 1) // 2

if total % 2 != 0:
    print("NO")
else:

    print("YES")
    set1 = []
    set2 = []

    if n % 4 == 0:

        i = 1
        while i <= n:
            set1.append(i)       # i
            set1.append(i + 3)   # i+3
            set2.append(i + 1)   # i+1
            set2.append(i + 2)   # i+2
            i += 4
    else:

        set1.append(1)
        set1.append(2)
        set2.append(3)

        i = 4
        while i <= n:
            set1.append(i)       # i
            set1.append(i + 3)   # i+3
            set2.append(i + 1)   # i+1
            set2.append(i + 2)   # i+2
            i += 4

    print(len(set1))
    print(*set1)

    print(len(set2))
    print(*set2)