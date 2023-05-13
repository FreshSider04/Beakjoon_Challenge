A, B, V = map(int, input().split())

# 도달하는 날을 x일이라고 했을 때, 총 올라가는 횟수는 x번, 내려오는 횟수는 (x-1)번이 될 것이다.
x = (V-B)/(A-B)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)
