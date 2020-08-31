# 1900~ 올해까지

import datetime
print("오늘: ", datetime.datetime.now().year)

year = datetime.datetime.now().year

#윤년인지 여부
#인터프리터 언어의 단점 : 변수명 중간에 틀려도 문법적 오류가 없으면 찾기가 어렵다.
leapCnt = 0
for i in range(1900, year+1):
    #i 가 연도가 들어오니까 윤년인지 확인
    # 윤년의 조건은 4의 배수이면서 100의 배수가 아니거나 400의 배수이거나 
    if i%4==0 and i%100!=0 or i%400==0:
        leapCnt = leapCnt +1 # 값이 누적되었다.

print("윤년의 개수: ", leapCnt)

