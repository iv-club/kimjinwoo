a = [2, 5, 1, 9, 7]
print(sorted(a))

b = 'zbdaf'
print("".join(sorted(b)))

c = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(c, key=len))

a = ['cde', 'cfc', 'abc']

def fn(s):
    return s[0], s[-1]

print(sorted(a, key=fn))

d = ['cde', 'cfc', 'abc']
print(sorted(a, key=lambda s: (s[0], s[-1])))


