N, K, M = map(float, input().split())

count = 0

if K >= M:
    while N >= K:
        X = K
        N -= X
        while X >= M:
            X -= M
            count += 1
        if X > 0:
            N += X
    print(count)
else:
    print(0)

