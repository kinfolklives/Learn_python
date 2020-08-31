# 문제1) 정수를 입력받아 첫 줄에 입력 받은 숫자를 출력하고 둘째 줄에 음수이면 “minus” 라고 

# 출력하는 프로그램을 작성하시오 

x = int(input("숫자 : ")) #str로 먼저 읽는다 

​

print(x)

if int(x)<0: #int로 바꾸어서 부호를 판단하거나 첫글자가 - 일 경우에 음수로 판단 가능하다

    print("minus")

​

# 문제2)나이를 입력받아 20살 이상이면 "adult"라고 출력하고 그렇지 않으면 몇 년후에 성인이 되는지를 

# "○ years later"라는 메시지를 출력하는 프로그램을 작성하시오.

​

​

# 문제3)복싱체급은 몸무게가 50.80kg 이하를 Flyweight 61.23kg 이하를 Lightweight, 72.57kg 이하를 

# Middleweight, 88.45kg 이하를 Cruiserweight, 88.45kg 초과를 Heavyweight라고 하자.

# 몸무게를 입력받아 체급을 출력하는 프로그램을 작성하시오.

weight = float(input("몸무게 : "))

if weight <=50.80:

    print("Flyweight")

elif weight <= 61.23:

    print("Lightweight")  

elif weight<=72.57:

    print("Middleweight")

elif weight<=88.45:

    print("Cruiserweight")

else:

    print("Heavyweight")

​

# 문제5)두 개의 실수를 입력받아 모두 4.0 이상이면 "A", 모두 3.0 이상이면 "B", 아니면 "C" 라고 

# 출력하는 프로그램을 작성하시오.

​

# 문제6) 영문 대문자를 입력받아 'A'이면 “Excellent”, 'B'이면 “Good”, 'C'이면 “Usually”, 

# 'D'이면 “Effort”, 'F'이면 “Failure”, 그 외 문자이면 “error” 라고 출력하는 프로그램을 

# 작성하시오.

​

# 
