# 작음 따옴표 3개를 사용해도 동일함 : 여러줄로 이루어진 문자열을 처리할 대 사용
print("""동해물과 백두산이 마르도 닮도록 하느님이
보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세""")

print("i'm \"junny\"")

# 이스케이프 문자 사용하기
print("서울시\t강남구\t역삼동\t")
print("사과\r바나나\r오렌지")

# 인덱싱 : 인덱스는 항상 0에서 부터 시작함
jumin = "990316-1234567"
print("gender : " + jumin[7]) # 1은 남성
print("brithyear : " + jumin[:2]) # 시작 인덱스를 주지 않으면 0에서 시작하고 end는 미만 개념이 있음
print("month : " + jumin[2:4]) # 2 이덱스부터 4 미만
print("day : " + jumin[4:6])

print("bd : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])

print("Hello"[0])
print("Hello"[:2])
print("Hello"[-3:])
print("Hello"[7:])

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

# 문자열 변경하기 : replace("","")
input_str = "Hello, Python Program"
new_str = input_str.replace("Python", "React")
print(new_str)

# 문자열에 포함된 문자 갯수 세기 및 문자열 길이
# 갯수 세기 : count()
# 길이 반환 : __len__(), len()
print(input_str.count("l")) # "l" 문자가 몇번 나오는지 갯수 세기
print(len(input_str)) #len() 함수 사용
print(input_str.__len__()) # 문자열에 포함된 내장 함수를 사용

# 문자열 찾기 : find(), rfind(), index()
# find() : 찾은 문자열의 첫번째 인덱스 반환, 문자열을 찾지 못하면 -1을 반환
# index() : 찾은 문자열의 첫번재 인덱스 반환, 문자열을 찾지 못하면 ValueError 라는 예외를 발생 시킴

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장")) # 뒤에서 부터 찾지만 인덱스는 앞에서 부터 센다
print(phrase.index("가장"))
# 없는 문자열 찾기
print(phrase.find("나에게"))
# print(phrase.index("나에게"))

new_phrase = phrase.replace("가장", "나에게")
print(new_phrase)

# 문자열 연산자
# "문자열" + "문자열"
# "문자열" * 3 : 뒤에 오는 숫자만큼 문자열을 반복
print("태양고" + "나희도")
# print("태양고" + 2) # 이건 안됩니다. 문자열과 정수를 더하는 것은 안됨
print("안녕하세요" * 3) # 정상 출력 됩니다. 문자열을 뒤에 수만큼 반복하라는 의미
print("안녕하세요", "!"*5,  "\n", "\t", "="*3, "태양고", "="*3, "\n나희도" * 3, "입니다")
print("안녕하세요", "!"*5,  "\n", "\t", "="*3, "태양고", "="*3, "\n고유림" * 3, "입니다", sep="")

# 문자열 양옆의 공백 제거 : strip()
input_a = """
    Hello.
studying about str
"""
print(input_a.strip())

