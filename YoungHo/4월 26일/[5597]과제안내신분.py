register = [x for x in range(1, 31)]
okHW_list = []

for _ in  range(0, 28):
    in_HWon = int(input())
    okHW_list.append(in_HWon)
non_HW = list(set(register) - set(okHW_list))

print(min(non_HW))
print(max(non_HW))