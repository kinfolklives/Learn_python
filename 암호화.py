key = "EARCFGJPKILOMDZTQSWBUVXNYH"
s = "I like star"

#암호화 하는 함수 :  encode 
def encode(s): #문자열 입력받아서 암호화된 문자열을 반환하도록 하면 됩니다 
    sResult = ""
    for c in s: #s라는 문장으로 부터 한글자씩 읽어서 c한테 전달을 한다 
        
        # if c =='a' : index = 0 
        # if c =='B' or c=='b': index = 1 
        # if c =='C' or c=='c': index = 2 
        # if c =='D' or c=='d': index = 3
        # ...............
        # A - 65  - 65 = 0 
        # B - 66  - 65 = 1
        # C - 67  - 65 = 2

        # a - 97  - 97 = 0 
        # b - 98  - 97 = 1 
        # c - 99  - 97 = 2 

        if ord(c)>=ord('A') and ord(c)<=ord('Z'):
            index = ord(c) - ord('A')
            ch = key[index] 
        elif ord(c)>=ord('a') and ord(c)<=ord('z'):
            index = ord(c) - ord('a')
            ch = key[index] 
        else:
            ch = c # 공백처리
        
        sResult = sResult + ch
    return sResult #함수가 일을 끝냈으면 결과값을 반환시키자 

#복호화 함수 :  decode 

s1 = encode(s)
print(s1)
