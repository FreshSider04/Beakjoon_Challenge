T = int(input())

for i in range(0, T):
    R, S = input().split()
    for j in range(0, len(S)):
        print(S[j] * int(R), end="")
        
    print()