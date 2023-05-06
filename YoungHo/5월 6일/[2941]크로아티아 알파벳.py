croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    # .replace( , )
    # ~를 ~로 대체하라
    word = word.replace(i, '*')
print(len(word))