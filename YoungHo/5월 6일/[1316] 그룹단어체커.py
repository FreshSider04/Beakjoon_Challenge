n = int(input())

remove_result = []
result = []
for _ in range(n):
    word = input()
    remover = list(word)
    for value in remover:
        if value not in remove_result:
            remove_result.append(value)
    result_word = ''.join(i for i in remove_result)
    result.append(result_word)
    remove_result = []

set(result)
print(len(result))

