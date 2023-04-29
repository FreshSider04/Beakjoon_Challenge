N = int(input())
string = str(input())
list1 = [string[i, i+2] for i in range(0,len(string), 1)]

hap = 0

for i in range(0, N):
    list_value = list_N[i]

    hap += list_value

print(hap)

