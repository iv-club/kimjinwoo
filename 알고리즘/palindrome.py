# 리스트로 해결
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum(): # 영문자, 숫자 여부를 판별
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

import collections

# 데크로 해결(속도가 리스트보다 좀더 빠름)
def isPalindrome(self, s: str) -> bool:
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

# 슬라이싱 사용
import re

def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # 슬라이싱, 뒤집음.


