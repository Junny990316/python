# 표준입력 input() : 사용자의 입력을 받아 그 값을 프로그램에서 사용하고자 할 때 사용
# 입력 받은 데이터는 문자열로 반환되며, 원하는 데이터 형으로 전달 받기 위해서는 형변환 필요
# print("input your name : ", end="")
# name = input()
# print(f"your name is {name}")

# name = input("input your name : ")
# age = int(input("input your age : "))
# addr = input("address : ")
# score = float(input("score : "))

# print(f"Hello. {name} your age is {age}")
# print(f"ur address is {addr} and score is {score}")

# 여러개의 데이터를 한번에 입력받기
# split() : 입력 받은 문자열을 공백 기준으로 분리하여 변수에 넣어주는 역할
# map() : 리스트 요소를 지정된 함수로 처리하는 함수

# str1, str2 = input("type in your name and addr : ").split()
# print(f"first string : {str1}, second string : {str2}")

# score = list(map(int, input("there's no limit : ").split()))
# print(score)

# 시간을 입력 받아 이쁘게 출력
hour, min, sec = map(int, input("h:m:s ").split(":"))
if hour > 12 :
    hour -= 12
    print(f"pm{hour:02}h{min:02}m{sec:02}s")
else :
    print(f"am{hour:02}h{min:02}m{sec:02}s")