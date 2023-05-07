system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split()) # N은 숫자, B는 진법
answer = ''

while N != 0: #N이 0이 아닐 떄 까지
    # N = 10, B = 2라고 가정
    # % :: 0 --> system[0] --> 0 --> answer = '0'
    # // :: 5 -> N = 5 

    # 5 % 2 == 1 --> answer = '01'
    # N =2

    # 2 % 2 == 0 --> answer = '010'
    # N = 1

    # 1 % 2 = 1 --> anser = '0101'
    # N = 0 --> 종료
    answer += str(system[N % B]) 
    N //= B

# 1010 :: 8 + 2 = 10 
print(answer[::-1])