# while 문 : 조건이 참인 동안 반복 수행하며 주로 횟수가 정해해지지 않은 경우에 사용, 횟수가 정해지지 않은 경우 반드시 탈출 조건이 필요
# n = int(input("정수 입력 : "))
# sum = 0
# while n:
#     sum += n # sum = sum + n
#     n-= 1
# print(sum)

# 유효값 체크
# while True :
#     age = int(input("나이 입력 : "))
#     if 0 < age < 200 : break; # 정상적인 입력으로 간주
#     print("나이를 다시 입력하세요.")

# for 요소 in 시퀀스(리스트, 튜플, 문자열) : 요소를 순회
# fruits = ["apple", "banana", "kiwi"]
# for e in fruits :
#     print(e)

# for 변수 in range(시작값, 종료값, 증감값) : 자바의 기본적인 for문과 동일
# n = int(input("정수입력 : "))
# sum = 0
# for i in range(1, n+1) :
#     sum += i
# print(sum)

# 2중 for 문 : 구구단 출력
# for i in range(2, 10): # 2 ~ 9
#     for j in range(1, 10) :
#         print(f"{i} * {j} = {i * j}")
#     print("-"*25)

# 2중 for문과 조건문 활용하기
