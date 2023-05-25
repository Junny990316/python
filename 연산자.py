# 산술연산자 : 더하기, 빼기, 곱하기, 나누기, 나머지, 몫, 제곱
i, j = 10, 3

# print("%d + %d = %d"%(i, j, i+j))
# print("%d - %d = %d"%(i, j, i-j))
# print("%d * %d = %d"%(i, j, i*j))
# print("%d / %d = %.2f"%(i, j, i/j))

# print(i / j) # 나누기 연산자
# print(i // j) # 몫 연산자
# print(i ** j) # 제곱 연산자

# tax_rate = 0.10
# income = int(input("당신의 수입을 입력하세요 : "))
# print(f"당신이 내야할 세금은 {income * tax_rate} 입니다")

# month_pay = float(input("당신의 월 실수령액을 입력하세요 : "))
# print(f"당신의 연봉은 {month_pay * 12 * 1.15:.2f}")

# 관계 연산자 (and, or, not), 대부분의 경우 비교연산자와 함께 사용되며, 참과 거짓을 판별
# and : 둘 다 참인경우 true
# or : 하나만 참인 경우 true
# not : 현재 조건을 부정하는 것
x, y, z = 10, 20, 30
rst1 = (x > 0) and (x > y) # false
rst2 = (x > 0) or (x > y) # true
rst3 = not((x > 0) or (x > y)) # false

# print(rst1, rst2, rst3)

# 나머지 연산자와 다항연산자
# (조건식) and 참인경우 or 거짓인 경우
# num = int(input("정수값 입력 : "))
# flag = (num % 2 == 0) and "even" or "odd"
# print(flag)

age = 23
is_adult = (age >= 20) and "adult" or "not adult"
print(is_adult)