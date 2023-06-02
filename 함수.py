# 함수란 ? 특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램을 의미
# 함수의 사용 목적은 재사용성과 모듈화를 위해 사용
# 업무 분담의 기준으로 삼을 수 있으며, 단위 테스트의 시준이 됨
# 일반적으로 함수는 식별자 뒤에 ()가 있음
# 매개변수와 함수를 호출하는 인자의 개수는 일치해야 함

# 매개변수가 있고 반환 타입이 없는 함수
# def name_card(name, addr, phone) :
#     print(f"주소 : {addr}")
#     print(f"전화번호 : {phone}")
#     print(f"이름 : {name}")

# name_card("Junn", "Seoul", "010-1234-1233")
# name_card("Jone", "Seoul", "010-1234-1333")

# 은행 계좌 개설하고 입금과 출금 예제
# def open_account(name) :
#     print(f"{name}님의 계좌가 개설되었습니다.")
#     return name
# def diposit(balancem input()) : # 잔액과 입금 금액을 입력 받음
#     print(f"{input}이 입금 되었습니다. 잔액은 {balancem + input} 입니다")
#     return balancem + input

# 출금
# def withdraw(balance, input) :
#     if balance >= input :
#         print(f"{input}이 출금 되었습니다. 잔액은{balance - input} 입니다")
#         return balance - input
#     else :
#         print(f"잔액이 부족합니다")
#         return balance

balence = 0 # 외부에서 선언하지만 매개변수로 전달
# name = open_account("Jonh")
# balence = diposit(balence, 1000)
# balence = withdraw(balence, 500)
# print(f"{name}의 잔액은 {balence} 입니다.")

# 기본값 인자 : 함수 선언 시 매개변수 대한 기본 값을 정의할 수 있음
def profile(name, year = 2, age = 19, school = "UBC") :
    print(f"이름 : {name}, 학교 : {school}, 학번 : {year}, 나이 : {age}")

profile("나희도")
profile("고유림")
profile("백이진", None, 22)

# 가변 매개변수 : 함수의 매개변수 앞에 (*) 붙여주면 함수의 매개변수를 몇개를 입력하든 함수 내에서 튜플로 인식
# def profile(name, age, *lang) :
#     print(f"이름 : {name}, 나이 : {age}", end=" ")
#     for e in lang :
#         print(e, end=" ")

# profile("나희도", 19, "Python", "Java", "C", "C++", "React", "Kotlin")
# profile("조세호", 36, "Python", "Java", "C", "C++", "React", "DB")
# profile("유재석", 48, "Python", "Java", "C",)

# 지역 변수와 전역 변수
# 전역 변수 : 함수 보다 변수의 생존 범위가 더 넓어서 리턴 값이 필요 없음
# global 키워드를 사용하면 전역으로 선언한 변수를 함수 내에 사용 할 수 있음

# knife = 10 # 칼 10자루 준비 함
# def game (player) :
#     global knife
#     knife -= player # 게임에 참가한 선수가 사용한 갯수만큼 차감

# def game2(player, knife) :
#     knife -= player
#     print(f"남아있는 칼은 {knife}자루 입니다")

# player = int(input("경기에 참여하는 선수가 몇명입니까? "))
# game2(player, knife)
# print(f"남아있는 칼은 {knife}자루 입니다")

# 람다와 함수
# 람다란 ? 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현, 이름 없는 함수를 의미
# def add(a, b) :
#     return a + b
# print(add(10, 20))

# print((lambda a, b : a + b)(1,2)) # 위 코드를 한줄로 표현

def power(n) :
    return n * n
 
square = lambda x : x * x # 람다식으로 익명의 함수 만들기

input = [1,2,3,4,5,6,7,8,9,10]

output = list(map(square, input))
print(output)