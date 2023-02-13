troom, tcond = map(int, input().split())
rwork = input()

if rwork == "freeze":
    if troom > tcond:
        print(tcond)
    elif troom <= tcond:
        print(troom)
elif rwork == "heat":
    if troom < tcond:
        print(tcond)
    elif troom >= tcond:
        print(troom)
elif rwork == "auto":
    print(tcond)
elif rwork == "fan":
    print(troom)
