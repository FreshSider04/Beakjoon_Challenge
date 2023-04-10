N, X = map(int, input().split())
set_A = list(map(int, input().split()))
for i in range(N):
    if set_A[i] < X:
        print(set_A[i], end=" ")