lst = [float(input()), float(input()), float(input()), float(input()), float(input())]

flag = 0

for i in range(3):
    for j in range(i + 1, 3):
        if (lst[i] <= lst[3] and lst[j] <= lst[4]) or (lst[j] <= lst[3] and lst[i] <= lst[4]):
            flag = 1
            break

if flag == 1:
    print("YES")
else:
    print("NO")
