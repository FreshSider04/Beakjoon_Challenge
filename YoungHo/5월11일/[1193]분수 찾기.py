n = int(input())

# 규칙
# 짝수라인은 시작점에서 끝점으로 갈수록  || 분자가 1씩 늘어가고 분모가 1씩 감소하며
# 홀수라인은 시작점에서 끝점으로 갈수록  || 분자가 1씩 줄어들고 분모가 1씩 늘어난다.
# 그래서 내가 구하고자 하는 수가 몇번째 라인에 있는지, 그 중에서 몇 번째 인덱스에 있는지를 알면 된다.


line = 0
#end는 그 라인의 마지막 인덱스를 뜻한다. ( 1, 3, 6, 10 ... )
end = 0
while n > end: #n이 마지막 인덱스보다 크면 
    # 라인 + 1
    line += 1 
    end += line 

diff = end - n 

if line % 2 == 0: #짝수 라인 일때
    top = line - diff 
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))

