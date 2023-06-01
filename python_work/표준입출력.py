print(39) # 정수형
print("문자열")
print([1,2,3,4]) # 리스트형
print(1+2)
print("파" + "이" + "팅")
print("파""이""썬")
print("파", "이", "썬") # 콤마는 기본적으로 띄어쓰기가 포함되어 있음
print("파\n\n\n이\n\n\n썬")
print("\"안녕하세요\"라고 말함")

# and 와 sep 옵션
print("Hello", end="\t")
print("python...")

print(1,2,3,4,5, sep="\t")

print("010","1234","5678", sep="-")

year = 2023
month = 5
day = 24
print(year, month, day, sep="/")

# 다양한 출력 스타일
name = "junny"
age = 25
gender = "F"
job = "couchPotato"
addr = "Seoul"
# C언어 스타일, %로 서식을 지정하는 형식
print("="*5, "C style", "="*5)
print("name : %s" %(name))
print("age : %d"%(age))
print("gender : %s"%(gender))
print("job : %s"%(job))
print("addr : %s"%(addr))

# python style : 3.6 이전 버전에서 주로 사용
print("="*5, "python old style", "="*5)
print("name : {}, addr : {}".format(name, addr))
print("age : {}".format(age))

# python style : 3.6 이후 스타일
print("="*5, "python new style", "="*5)
print(f"name : {name}") #f 반드시 넣어줘야함
print(f"age : {age}")
print(f"gender : {gender}")
print(f"job : {job}")
print(f"addr : {addr}")

# java style
print("="*5, "java style", "="*5)
print("name : " + name)
print("age : " + str(age)) # 문자열로 형 변환
print("gender : " + gender)

# 출력 포맷 정렬
# < : 좌측 정렬
# > : 우측 정렬
# ^ : 중앙 정렬
print("|{:6}|".format(10))
print("|{:<6}|".format(10))
print("|{:>6}|".format(10))
print("|{:^6}|".format(10))

num = 10
print(f"|{num:5}|")
print(f"|{num:<5}|")
print(f"|{num:>5}|")
print(f"|{num:^5}|")

# 소수점 이하 자르기
print(f"{3.141592:.2f}")