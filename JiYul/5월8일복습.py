#def 함수이름() :
#함수 코드(들여쓰기)
#def : ‘definition’의 줄임말로, 함수를 정의
#함수가 호출되기 전에 반드시 정의
#pass 예약어 : 함수의 헤더만 결정하고 몸체는 나중에 작성하고 싶은 경우 사용
if True:
    pass
else:
    print(false)
#만약 pass를 쓰지 않는다면 오류가 발생한다.
def main():
    radius = int(input('원의 반지름:'))
    result = get_area(radius)
    print(result)
    
def get_area(radius):
    area = 3.14*radius**2
    return area

main()
#에라토스테네스 체 알고리즘 소수 구하기
def main():
#함수 정의
    n = int(input('1부터 소수를 구할 수를 입력:'))
    print(f'1부터 {n}까지 소수의 갯수는:{prime_era(n)}')
#주 함수는 input() 함수를 사용하는 사용자로부터 정수 'n'을 얻는다.
#그런 다음 prime_era 함수를 호출하여 'n'의 값을 인수로 전달한다.
    
def prime_era(n):
#정의
    number = [False, False]+[True]*(n-1)
    #prime_era 함수는 'number'라는 부울 값 목록을 초기화합니다. 여기서 처음 두 요소(0 및 1)는 소수가 아니므로 'False'로 표시됩니다.나머지 요소는 다르게 증명될 때까지 소수라고 가정하여 '참'으로 표시됩니다.
    primes = []
    for i in range(2, n+1):
#for문
        if number[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                number[j] = False
    return len(primes)
#모든 숫자를 확인한 후 함수는 1과 'n' 사이에서 발견된 소수의 수를 나타내는 '소수' 목록의 길이를 반환
main()
#디폴트 인수 : 함수의 매개변수가 기본값을 가질 수 있다
#가변인수( * ):함수는 전달하는 값이 몇 개 인지 모른다. 함수 안에서 전달되는 값의 개수를 파악
#lambda 매개변수 : 표현식
#람다(lambda) 함수
#함수의 이름 없이 함수처럼 사용할 수 있는 익명의 함수로 람다 표현식