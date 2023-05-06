# 팰린드룸 : 영단어를 앞뒤로 뒤집어도 같은 단어
word = input()

if word == word[::-1]:
    print(1)
else:
    print(0)