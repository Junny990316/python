# 이름입력
# 나이입력 : 1 ~ 199까지 입력 받고 잘못된 값이 나오면 재 입력 요청
# 성별입력 : 영문자로 입력 받고 나머지는 재 입력 요청
# 직업입력 : 1 학생, 2 회사원, 3 주부, 4 무직으로 입력 받고 재 입력 요청
# 결과는 마지막에 출력

name = input("이름 : ")

while True:
    age = int(input("나이 : "))
    if 0< age < 200:
        break
    else:
        print("잘못된 값입니다. 다시 입력해주세요.")

while True :
    gender = input("성별 ex)M, F : ")
    if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f' :
        break
    else :
        print("잘못된 값입니다. 다시 입력해주세요.")

while True :
    job = input("직업 입력 1 학생, 2 회사원, 3 주부, 4 무직 : ")
    if job.isdigit() : # 숫자가 값으로 들어왓는지 확인함
        job = int(job)
        if 0 < job < 5 : break
    print ("잘못된 값입니다. 다시 입력해주세요")

if gender == 'M' or gender == 'm' : gender_prn = "남성"
else : gender_prn = "여성"

job_name = ["", "학생", "회사원", "주부", "무직"]

print("="*5, "회원정보", "="*5)
print("이름:", name)
print("나이:", age)
print("성별:", gender_prn)
print(f"직업: {job_name[job]}")