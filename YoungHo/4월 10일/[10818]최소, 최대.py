N = int(input())

# 주의점!
# map(int, list(input().split()))시 주소 나옴!
list1 = list(map(int, input().split()))

print(min(list1), max(list1))