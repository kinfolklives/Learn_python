# a = [0]*3 #행이 된다. 
# for i in range(0, len(a)):
#     a[i] = [0]*2

# k=1 
# for i in range(0, len(a)):
#     for j in range(0, len(a[i])):
#         a[i][j] = k 
#         k = k+1 

# for i in range(0, len(a)):
#     for j in range(0, len(a[i])):
#         print(a[i][j], end=' ')
#     print()
i = 0
a = [0]*10 #행이 된다. 
for i in range(0, len(a)):
    a[i] = [0]*i

k=1 
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        a[i][j] = k 
        k = k+1 
    
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=' ')
    
    print()

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