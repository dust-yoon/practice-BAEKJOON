import datetime
time = datetime.datetime.today() + datetime.timedelta(hours=9)
print(time.strftime('%Y-%m-%d'))


# <사고과정>

# 1. UTC의 날짜 확인
#     datetime.datetime.today()
# 2. 9시간을 더해 서울의 날짜 설정하기
#     datetime.timedelta(hours=9)
# 3. time 출력
#     sfrftime('%Y-%m-%d')

print("       _.-;;-._")
print("'-..-'|   ||   |")
print("'-..-'|_.-;;-._|")
print("'-..-'|   ||   |")
print("'-..-'|_.-''-._|")