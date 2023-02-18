a = float(input())
b = float(input())
c = float(input())

if c < 0:
    print("NO SOLUTION")
else:
    if a == 0:
        if b == c * c:
            print("MANY SOLUTIONS")
        else:
            print("NO SOLUTION")
    else:
        if (c * c - b) / a == int((c * c - b) / a) and (a * ((c * c - b) / a) + b) >= 0:
            print(int((c * c - b) / a))
        else:
            print("NO SOLUTION")
