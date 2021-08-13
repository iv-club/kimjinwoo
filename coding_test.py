a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False) # 2 진수에서는 실수 값을 더하면 미세한 오차가 발생 -> round() 함수로 해결 가능

a = [1, 2, 3, 4, 5]
print(a)

print(a[3]) # 4번째 원소 출력

n = 10
a = [0] * n # 크기가 n이고, 모든 값이 0인 1차원 리스트 a를 초기화
print(a)

# 다섯 번째 원소만 출력
print(a[4])

# 뒤에서 첫 번째 원소 출력
print(a[-1]) 

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 두 번째 원소부터 3번째 까지 출력
print(a[1 : 4]) 

# 리스트 컴프리헨션
# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)] 

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

# 0 부터 19까지의 수중에서 홀수만 포함하는 리스트
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)

# "Hello World"를 5번 출력하기
for _ in range(5):
    print("Hello World")

# a = (1, 2, 3, 4)
# print(a)
#
# a[2] = 7 # 튜플은 값을 변경할 수가 없으므로 에러 발생

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    key_list = data.keys()
    value_list = data.values()

for key in key_list:
    print(data[key])

data = set([1, 1, 2, 3, 4, 4, 5])

n, m, k = map(int, input().split())

#import sys

#data = sys.stdin.readline().rstrip()
#print(data)

a = 1
b = 2
print(a, b)
print(7, end=" ")
# end를 이용하여 줄바꿈을 하지 않고 공백으로 구분

answer = 7
print("정답은 " + str(answer) + "입니다.")
# 정수형을 문자열로 변환하여 + 연산을 해줌

#f-string 예제
print(f"정답은 {answer}입니다.")
#접두사 f를 이용하여 중괄호 안에 변수명을 넣고 정수와 문자열을 함께 사용할수 있다.

score = 85

if score >= 70:
    print('성적이 70점 이상입니다.')
    if score >= 90:
        print('우수한 성적입니다.')
else:
    print('성적이 70점 미만입니다.')
    print('조금 더 분발하세요.')

print('프로그램을 종료합니다.')

a = -15

if a >= 0:
    print("a >= 0")
elif a >= -10:
    print("0 > a >= -10")
else:
    print("-10 > a")

if True or False:
    print("Yes") #or 대신 and면 아무것도 출력이 안됨

score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

array = [9,8,7,6,5]

for x in array:
    print(x)

result = 0
for i in range(1, 31):
    result += i

print(result)

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i*j)
    print()

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

print((lambda a, b: a + b)(3,7))

array = [('김진우', 50), ('홍길동', 32), ('유길준', 74)]
print(sorted(array, key=lambda x: x[1]))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))

from itertools import combinations

data = ['a', 'b', 'c']
result = list(combinations(data, 2))
print(result)

from itertools import permutations

result = list(permutations(data, 3))
print(result)

from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter)) # 사전 자료형으로 반환