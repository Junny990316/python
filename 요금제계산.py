   # 요금제 계산
# 영식 요금제 : 30초에 10원
# 민식 요금제 : 60초에 15원
# 입력은 첫 줄에 통화 횟수를 입력 받고 다음줄 각 통화에 대한 통화 시간을 입력 받음
# 3
# 34 56 78

cnt = int(input("통화 횟수 : "))
call_time = list(map(int, input("통화 시간").split())) # 공백 기준으로 통화시간 입력 받기
y_payment = m_payment = 0 # 영식 요금제와 민식요금제 값을 초기화 시키기

for i in range(cnt) :
    y_payment += (call_time[i] // 30) * 10 + 10 # 통화를 시작함과 동시에 10원을 더해줘야 하므로 +10
    m_payment += (call_time[i] // 60) * 15 + 15

if y_payment > m_payment :
    print("M", m_payment)
elif y_payment < m_payment :
    print("Y", y_payment)
else :
    print("Y M", y_payment)