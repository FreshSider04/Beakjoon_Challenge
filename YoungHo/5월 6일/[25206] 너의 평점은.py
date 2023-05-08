grade_card = {}
for _ in range(20):
    subject, num, grade = map(int, input().split())
    grade_card[subject] = [num, grade]
