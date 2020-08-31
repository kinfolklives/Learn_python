key = "EARCFGJPKILOMDZTQSWBUVXNYH"
s = "I like star"

#암호화 하는 함수 : encode
def encode(s): #문자열 입력받아서 암호화된 문자열을 반환하도록 하면 됩니다.
    sResult= ""
    for c in s : #s라는 문장으로 부터 한글자씩 읽어서 c한테 전달을 한다.
        # if c =='A' or c == 'a' : index = 0
        # if c =='B' or c == 'b' : index = 1
        # if c =='B' or c == 'b' : index = 2
        # if c =='B' or c == 'b' : index = 3
        # ----------------
        # A - 65 - 65 = 0
        # B - 66 - 65 = 1
        # C - 67 - 65 = 2
        # a - 97 - 65 = 32
        # >> a - 97 - 97 = 0
        if ord(c) >=ord('A') and ord(c)<=ord('Z'):
            index = ord(c) - ord('A')
            ch = key[index]
        elif ord(c)>=ord('a') and ord(c)<= ord('z'):
            index = ord(c) - ord('a')
            ch = key[index]
        else:
            ch = c # 공백처리
    
        sResult = sResult + ch 
    return sResult #함수가 일을 끝냈으면 결과값을 반환시키자.

#복호화 하는 함수 : decode
def decode(s):
    sResult=""
    for c in s:
        #각 글자가 key 배열에 어디에 위치하고 있는지를 찾으면 된다. 
        if c in key: # 존재 안할경우는 바꿀 필요가 없다.
            index = key.index(c)
            #index를 문자로 되돌리기
            # 0 + 'A'  = 'A'
            # 1 + 'A'  = 'B'
            ch = chr(index + ord('A'))
            # print( 1 + ord('A') )
            # print( 2 + ord('B') )
        else:
            ch = c
        sResult = sResult + ch 
    return sResult

s1 = encode(s)
print("암호화: ", s1)
s2 = decode(s1)
print("복호화: ", s2)

for i in range(1, 129):
    print(i, chr(i))
