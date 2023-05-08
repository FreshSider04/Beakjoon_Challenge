# 쿼터(Quarter, $0.25)
# 다임(Dime, $0.10)
# 니켈(Nickel, $0.05)
# 페니(Penny, $0.01)
T = int(input())
MoneyCase = []
for _ in range(T):
    # if 101 cent ==  0.25 * 4 + 0.01 * 1
    # 단위:: 센트(=0.01$)
    MoneyCase.append(int(input()))

for i in range(0, T):
    print(MoneyCase[i] // 25,end= " ")
    Dime = MoneyCase[i] % 25

    print(Dime // 10,end=" ")
    Nickel = Dime % 10

    print(Nickel // 5,end=" ")
    penny = Nickel % 5
    
    print(penny // 1)