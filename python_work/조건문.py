# 조건문 : if ~ else
# num = int(input("정수를 입력하세요 : "))
# if num % 2 == 0 :
#     print("even number")
# else :
#     print("odd number")

# 조건문 : if ~ elif ~ else
# n = int(input("정수 입력 : "))
# if n > 100 :
#     print("100보다 큼")
# elif n < 100 :
#     print("작음")
# else :
#     print("같음")

# print("지금 계절은? : ", end='');
# season = input()
# if season == "spring": print("봄이 왔어요.")
# elif season == "summer": print("여름이 왔어요.")
# elif season == "fall" or season == "autumn" : print("쓸쓸한 가을 입니다.")
# elif season == "winter": print("아직 겨울이네요ㅠㅠ")
# else : pass

# age = int(input("age : "))

# if(age > 0 and age < 100) :
#     print("정상입력")
# else :
#     print("잘못 입력")

# 회원 가입을 위한 아이디와 패스워드를 입력 받기
# string.find(찾을 문자)
# string.find(찾을 문자, 시작 Index)
# string.find(찾을 문자, 시작 Index, 끝 Index)
user = input("ID : ")
if len(user) >= 10 :
    pw = input("PWD : ")
    if pw.__len__() < 8 or pw.__len__() > 16 :
        pass
    else :
        print(f"아이디 : {user}")
        print(f"비밀번호 : {pw}")
else :
    print("아이디는 반드시 10자리 이상이어야 합니다")
