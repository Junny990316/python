# 집합은 주로 다른 자료형의 중복 제거 할 때 자주 사용합니다.
# 순서가 없음, 중복 불가, mutable(읽기, 쓰기) 특성

# 중복 제거 
s1 = set([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])
# print(s1)

# 교집합 : 양쪽에 모두 존재하는 요소만 선택
s2 = set([1,2,3,4,5])
s3 = set([1,3,5,7,8,9])

# print(s2.intersection(s3))

# 합집합
# print(s2.union(s3))

# 차집합 (앞에서 뒤를 빼는 것)
# print(s2.difference(s3))

# 중복제거로 로또 번호 만들기
import random
lotto = set()
while True : # 무한의 반복을 돌릴 필요가 없음 굳히 while 쓸 필요가 없다는 뜻
    num = random.randrange(1, 46)
    lotto.add(num)
    if len(lotto) == 6 : break

print(lotto)