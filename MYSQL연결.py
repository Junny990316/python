import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="heo0365010", db="mysqlDB", charset="utf8")

# 전역변수
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""


# 메인 코드
conn = pymysql.connect(host="127.0.0.1", user="root", password="heo0365010", db="mysqlDB", charset="utf8")


# 커서 생성하기
cur = conn.cursor()
# 데이터 입력 하기
# cur.execute("INSERT INTO userTable VALUES('ayj', '안유진', 'ayj@gmail.com', 2003)")
# cur.execute("INSERT INTO userTable VALUES('jwy', '장원영', 'jwy@gmail.com', 2004)")

while True :
    data1 = input("아이디 : ")
    if data1 == "" : break
    data2 = input("이름 : ")
    data3 = input("이메일 : ")
    data4 = input("생년월일 : ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', '" + data4 + "')"
    cur.execute(sql)


# 데이터 저장하기
conn.commit()

# 연결 종료하기
conn.close()