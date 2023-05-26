# n = list(map(int, input("정수 입력 : ").split()))
# result = sum(n)
# print(f"average : {result / len(n)}")

# 정수 n을 입력 받아 n * n 출력하기
# n = input("정수 입력 : ")
# result = int(n) * int(n)
# print(result)

# n에 대한 숫자를 입력 받아 최대값 최소값
# n = list(map(int, input("정수 입력 : ").split()))
# print(max(n))
# print(min(n))

# 주민등록번호를 입력 받아 생년월일, 성별, 나이 출력
num = input("주민번호를 입력 : ")

year = int(num[:2])
month = num[2:4]
date = num[4:6]
gender = num[6]

if gender == '1' or gender == '3' :
    gender = 'male'
else :
    gender = 'female'

age = 2023 - (1900 + year) + 1


print(f"생년월일 : {year}{month}{date}")
print("성별 : {0}".format(gender))
print(f"나이 : {age}")