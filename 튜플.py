# 튜플이란 ? 변경할 수 없는 시퀀스 자료형, ()괄호를 사용하여 생성
# 패킹과 언패킹 개념이 있음
# 튜플 정의하기

person = ("Junny", 25, "Seoul") # () 괄호 생략 가능, 쓰기 불가 특성

# 튜플 언패킹 하기 (구조분해랑 비슷함)
# name, age, city = person
# print(name)
# print(age)
# print(city)

# 튜플을 이용한 함수 반환값 다루기
def get_person() :
    name = "Junny"
    age = 25
    city = "Seoul"
    return name, age, city

# result = get_person() # 튜플의 패킹 동작
# print(result)

a, b, c = get_person()
# print(a, b, c)

# 기본적인 동작
tp = 1,2,3,4,5,6,7,8,9,10,1,1,2,2,3,3
print(tp.count(7)) # 원하는 데이터의 개수를 새어주는 함수
print(tp.index(10)) # 원하는 데이터의 시작 인덱스를 알려줌
print(len(tp)) # 튜플에 포함된 데이터의 개수
print(tp.__len__())

# 튜플에서 실행 되지 않는 것 (삭제는 안됨)
# del tp[0]