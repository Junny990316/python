# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성

result = ""
for e in input() : # input 개수만큼 for문을 반복함
    if e.islower() :
        result += e.upper()
    else :
        result += e.lower()
print(result)

# 세개의 자연수 입력받아서 모두 곱함
# 결과값에서 나오는 숫자의 획수를 출력하기
# 17037300 => 0은 3, 1은 1, 7 은 2번

a, b, c = map(int, input("정수 3개 입력 : ").split())
ls = list(str(a * b * c)) # 문자열로 형 변환

for i in range(10) : # 등장하는 숫자의 횟수를 구하기 때문에 0~9 10만큼 반복하기
    print(ls.count(str(i))) # 해당 문자의 개수 반환, 문자열로 형변환 했기에 str(i)로 형 변환 해주기
