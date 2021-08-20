a = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
for k, v in a.items():
    print(k, v)

a = dict()
a = {}

del a['key1']

import collections

a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
print(a)

a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)
print(b)
c = b.most_common(2) # Counter 객체에서 가장 빈도 수가 높은 요소 추출.
print(c)

d = collections.OrderedDict({'banana' : 3, 'apple' : 4, 'pear' : 1, 'orange' : 2})
print(d)
