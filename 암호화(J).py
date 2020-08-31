key = "EARCFGJPKILOMDZTQSWBUVXNYH"
init = 'A'

s = input("문자입력 : ")

enc = ""
for ch in s:
    if ch == ' ':
        enc += " "
    else:
        u = ch.upper()
        i = ord(u)-ord(init)
        enc += key[i]
print("encryption: ", enc)

dec = ""
for ch in enc:
    if ch == ' ':
        dec += " "
    else:
        i = key.index(ch)+ord(init)
        dec += chr(i)
print("decryption: ", dec)