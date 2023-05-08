n = int(input())

InAndOut = {}
for _ in range(n):
    a, b = map(str, input().split())
    InAndOut[a] = b

enter_list = []
for key, value in reversed(InAndOut.items()):
 if value == 'enter':
  enter_list.append(key)
num = len(enter_list)
reversed(enter_list)
for _ in num:
  print(enter_list)

