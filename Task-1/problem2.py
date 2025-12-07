
s = input().strip()

if s == "":
    print(0)
else:

    max_len = 1
    current_len = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
   
            current_len += 1
        else:

            current_len = 1


        if current_len > max_len:
            max_len = current_len

    print(max_len)