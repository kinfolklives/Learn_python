"""
정수를 10개쯤 입력받아서 합계를 구하고 싶다 
"""
def function1():
    numList = list()
    for i in range(1, 6):
        num = int(input("정수 {}번째 : ".format(i)))
        numList.append(num)
    print(numList)


#function1()
def function2():
    numList = [0]*5 #미리 확보하고 시작함 
    for i in range(0, 5):
        num = int(input("정수 {}번째 : ".format(i)))
        numList[i] = num 
    print(numList)

​

#function2()
#2차원  3 by 4행렬 3행, 4열을 만들어 쓰고자 할때
a = [[0]*4 ]*3 
a = [[0]*4, [0]*4, [0]*4]
print(a)

a[0][0]=1
a[0][1]=2
a[0][2]=3
a[0][3]=4

a[1][0]=5
a[1][1]=6
a[1][2]=7
a[1][3]=8

a[2][0]=9
a[2][1]=10
a[2][2]=11
a[2][3]=12

print(a)


a = [0]*10 #행이 된다. 
for i in range(0, len(a)):
    a[i] = [0]*10 
print(a)

k=1 
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        a[i][j] = k 
        k = k+1 

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=' ')
    print()


"""
1
2 3 
4 5 6 
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21 
22 23 .............

 1  2  3  4  0 
 5  6  7  8  0
 9 10 11 12  0
13 14 15 16  0
 0  0  0  0  0 
"""


a = [0]*10
b = [a[:] for i in range(1,11)]
k=1
for i in range(0,10):
    for j in range(0, i+1):
        b[i][j]=k 
        k = k+1 

for i in range(0, len(a)):
    for j in range(0, len(b[i])):
        print("%3d" % b[i][j], end=' ')
    print()


#2번문제풀이 
a = [
     [1,  2,   3,  4, 0],  #a[0][4] = a[0][4] + a[0][0] + a[0][1] + a[0][2] + a[0][3]
     [5,  6,   7,  8, 0],
     [9,  10, 11, 12, 0],
     [13, 14, 15, 16, 0],
     [ 0,  0,  0,  0, 0],
    ]

#행에 대한 합산 먼저하기 \
i=0
for i in range(0,4):
    for j in range(0, 4):
        a[i][4] += a[i][j]
print(a)

#열의 경우에는 a[4][0] = a[0][0]+a[1][0]+a[2][0]+a[3][0] 
#a[4][0] = a[4][0]  + a[0][0]+a[1][0]+a[2][0]+a[3][0]
for i in range(0,5):
    for j in range(0, 4):
        a[4][i] += a[j][i]
print(a)

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print("%3d" % a[i][j], end=' ')
    print()

"""
1차원배열 - 1d tensor 
2차원배열 - 2d tensor
3차원배열 - 3d tensor
4차원배열 - 4d tensor
5차원배열 - 5d tensor
"""

"""
로또번호생성 : 1~10 중에서 6개의 숫자를 랜덤하게 추출하기 
객체 지향을 이용해서 생성을 만들고 
실제 사용자가 로또 번호 입력하면, 맞을 개수를 반환
[5,3,2,9,10]
[1,9,4,2,3]   맞은개수 : 3, 6개면 1등 메시지 보여주기 
"""  