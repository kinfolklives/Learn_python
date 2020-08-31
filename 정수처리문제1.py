# 문제1) 정수를 입력받아 첫 줄에 입력 받은 숫자를 출력하고 둘째 줄에 음수이면 “minus” 라고 
# 출력하는 프로그램을 작성하시오. 숫자가 아닌 문자가 들어오면 error 라고 출력하라. 
num = input("입력: ")
def mydigit(num):
    print(int(num))
    if num[0] == '-':
        return ("minus")
    
print(mydigit(num))




