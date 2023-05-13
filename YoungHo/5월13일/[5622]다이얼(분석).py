# 다이얼을 리스트에 집어 넣는다.
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# 값을 입력한다.
a = input()

# 시간
ret = 0

# 문자열의 길이만큼 반복
for j in range(len(a)):
    # 다이얼 리스트 대입
    for i in dial:
        # 만약에 dial리스트에 a[j]가 있다면
        if a[j] in i:
            # ret은 +3
            ret += dial.index(i)+3
print(ret)