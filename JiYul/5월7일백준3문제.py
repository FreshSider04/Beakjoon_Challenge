#1330 두 수 비교하기
A,B = map(int,input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
#9498 시험성적
score = int(input())

if score >= 90 :
    print('A')
elif score >= 80 :
    print('B')
elif score >= 70 :
    print('C')
elif score >= 60 :
    print('D')
else:
    print('F')
#2753 윤년
year = int(input())

if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0):
    print('1')
else:
    print('0')