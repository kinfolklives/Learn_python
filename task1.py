# task 01-1
import datetime
d = datetime.datetime.now()
cur_year = int(d.year)
leapyear = list()

def leapYear_In():
    inp = int(input("년도 입력: "))
    for i in range(inp, cur_year+1, 4):
        if i%100 !=0 or i%400 ==0:
            leapyear.append(i)
    print(str(leapyear).strip('[]'))
    print("윤달의 개수는 {}입니다. ".format(len(leapyear)))

def leapYear():
    for i in range(1900, cur_year+1, 4):
        if i%100 !=0 or i%400 ==0:
            leapyear.append(i)
    print(str(leapyear).strip('[]'))
    print("윤달의 개수는 {}입니다. ".format(len(leapyear)))


#leapYear_In()
#leapYear()


# tast 01-2

pw = "ZABYCXDWEVFUGTHSIRJQKPLNMO"
inp = input("입력: ")
enc = ""

for c in inp:
    if c ==' ':
        enc = enc + " "
    else :
        u = c.upper()
        i = ord(u) - ord('A')
        enc = enc + pw[i]
print("암호화 : ", enc)

dec = ""
for c in enc:
    if c ==' ':
        dec = dec + ' '
    else: 
        i = pw.index(c) + ord('A')
        dec = dec + chr(i)
print("복호화 : ", dec)

# 2번은 조장님의 도움을 받아서 했습니다~
