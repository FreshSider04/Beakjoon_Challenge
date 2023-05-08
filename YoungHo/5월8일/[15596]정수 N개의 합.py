# Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
def main():
    n = int(input())
    def solve(n):
        a = [x for x in range(n+1)]
        print(sum(a))
    solve(n)
main()        