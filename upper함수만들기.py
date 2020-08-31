# # 'a' = 97, 'A' = 95 
# print (ord('a')-32)
# print (ord('b')-32)
# print (chr(ord('a')-32))

def upper(s):
    U = ""
    for c in s:
        #수문자일때만, 다른 문자들은 해당사항이 없다. 
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        U = U + c 
    return U  
print(upper("what are you doing?"))

def lower(s):
    L = ""
    for c in s:
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            c = chr(ord(c)+ 32)
        L = L + c 
    return L
print(lower("APPLE"))


# print(ord('1'))
# print(ord('2') -48)
# print(ord('0') -48)
# print(ord('1') -48)
# print(ord('2') -48))
# 1 = 49  / 1= 1

def myint(s):
    for c in s:
        if ord(c) >= ord("0") and ord(c) <= ord("9"):
            c = ord(c) -48
    return c
print(myint('9'))
print(type(myint('9')))

"""
print(ord(s[0])-48)
print(ord(s[1])-48)
print(ord(s[2])-48)

n1 = 0
n1 = n1 * 10 + ord(s[0]-48) = 0*10 + 49 -48 = 1
n1 = n1 * 10 + ord(s[1]-48) = 1*10 + 49 -48 = 2
n1 = n1 * 10 + ord(s[2]-48) = 12*10 + 49 -48 = 123
""" 
def myintB(s):
    n1 = 0
    for i in range(0, len(s)):
        n1 = n1 * 10 + ord(s[i])-ord("0")
    return n1
print(myintB('123')) 
print(myintB('12')+myintB('456'))
print("123" + "45") 