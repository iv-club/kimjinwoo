a, b = list(map(int, input().split())) # 나누어 입력
print(a+b)

# 입출력 가속
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

# 입력한 값만큼 반복해서 입력
MAP = [list(map(int, input().split())) for _ in range(int(input()))]

# 정수와 배열이 같은 줄일 때
N, *arr = map(int, input().split())


arr = [input() for _ in range(N)]
arr = [list(input()) for _ in range(N)]

# 공백없이 값 출력
arr = [1, 2, 3, 4]
print("".join(map(str, arr)))

arr = [1, 2, 3, 4]
print(*arr) # 숫자만 공백을 주고 출력

# 리스트 컴프리헨션
[n * 2 for n in range(1, 10 + 1) if n % 2 == 1]

# 딕셔너리
a = {key: value for key, value in original.items()}

# 제너레이터
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n
g = get_natural_number()
for _ in range(0, 100):
    print(next(g))

for i in range(5):
    print(i, end=' ')

#  순서를 부여하는 enumerate
list(enumerate(arr))

for i, v in enumerate(a):
    print(i, v)

# 몫과 나머지를 동시에 구하는 divmod()
divmod(5, 3)

# 콤마를 구분자로 지정
print('a', 'b', sep=',')

# 줄바꿈을 하지 않음.
print('aa', end=' ')
print('bb')

# 리스트를 공백으로 출력
a = ['a', 'b']
print(' '.join(a))

# fstring
idx = 1
fruit = "Apple"
print(f'{idx + 1}: {fruit}')

