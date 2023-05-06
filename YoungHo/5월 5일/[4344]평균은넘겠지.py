case_num = int(input())

for _ in range(case_num):
    case_value = list(map(int, input().split()))
    avg = sum(case_value[1:]) / case_value[0]

    count = 0
    for score in case_value[1:]:
        if score > avg:
            count += 1
    rate = count/case_value[0]*100
    print(f"{rate:.3f}%")