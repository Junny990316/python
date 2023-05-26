# 이름입력
# 나이입력 : 1 ~ 199까지 입력 받고 잘못된 값이 나오면 재 입력 요청
# 성별입력 : 영문자로 입력 받고 나머지는 재 입력 요청
# 직업입력 : 1 학생, 2 회사원, 3 주부, 4 무직으로 입력 받고 재 입력 요청
# 결과는 마지막에 출력

name = input("이름 : ")

while True:
    age = int(input("나이 : "))
    if age >= 1 and age <= 199:
        break
    else:
        print("잘못된 값입니다. 다시 입력해주세요.")

while True :
    gender = input("성별 ex)M, F : ")
    if age == ord('M', 'F') :
        break
    else :
        print("잘못된 값입니다. 다시 입력해주세요.")

while True :
    job = int(input("직업 입력 1 학생, 2 회사원, 3 주부, 4 무직 : "))
    if 0 < job and job < 5 :
        break
    else :
        print("잘못된 값입니다. 다시 입력해주세요.")

print("이름:", name)
print("나이:", age)
print("성별:", gender)
print("직업:", job)