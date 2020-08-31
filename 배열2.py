# a = [0]*10 #행이 된다. 
# for i in range(0, len(a)):
#     a[i] = [0]*10 
# print(a)

# k=1 
# for i in range(0, len(a)):
#     for j in range(0, len(a[i])):
#         a[i][j] = k 
#         k = k+1 
#         i = i+1

# for i in range(0, len(a)):
#     for j in range(0, len(a[i])):
#         print(a[i][j], end=' ')
#     print()

# a = [0]*10
# for i in range(0, len(a)):
#     for j in range(0, len(a[i])):
#         print(a[i][j], end=' ')
#     print()


# a = [0]*10
# b = [a[:] for i in range(1, 11)]
# k = 1
# for i in range(0,10):
#     for j in range(0, i+1):
#         b[i][j]=k
#         k = k+1
# for i in range(0, len(a)):
#     for j in range(0, len(b[i])):
#         print("%3d" % b[i][j], end=" ")
#     print()

