# 문제1) 정수를 입력받아 첫 줄에 입력 받은 숫자를 출력하고 둘째 줄에 음수이면 “minus” 라고 
# 출력하는 프로그램을 작성하시오. 숫자가 아닌 문자가 들어오면 error 라고 출력하라. 

# x = int(input("숫자 : ")) #str로 먼저 읽는다 
# print(x)

# if x<0: #int로 바꾸어서 부호를 판단하거나 첫글자가 - 일 경우에 음수로 판단 가능하다
#     print("minus")


# int 라는 함수가 만약에 문자가 들어가면, 예외가 발생되고 끝난다.
# x = input("숫자 : ")
# print(x)
# print(x.isdigit()) #숫자로 바꿀 수 있는지 확인하는 함수, 
                   # 숫자면 True, 숫자가 아닌 문자가 포함되면 False
# if x<0: 
#     print("minus")
# 0 -- 48
#부호있는 숫자가 주어지더라도 정수 > True,  아니면 > False

def mydigit(num):
    """
    첫번째가 -, + 부호비트가 와야함, 안올수도 있고, 첫번째index만 +, -, 0, 1,2,3,4,5,6,7,8,9
    나머지는 0,1,2,3,4,5,6,7,8,9
    """
    if num[0] not in ['+', '-', '0', '1','2','3','4','5','6','7','8','9']:
        return False
    for i in range(1,len(num)):
        if num[i] not in ['0', '1','2','3','4','5','6','7','8','9']:
            return False
    return True

print(mydigit("-5"))
print(mydigit("-50"))
print(mydigit("-328a1b11"))
print(mydigit("+32a45"))
print(mydigit("-32a.23"))



