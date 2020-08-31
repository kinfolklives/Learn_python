a = [1,2,3,4,5,6,7,8,9,10]
# 1번 답
print(a[::2])
# 2번 답
print(a[8::-2])

# 3번 답
s = "I like star. red star blue star green star"
print(s[::-1])
# 4번답
x = s.replace("star", "moon")
print(x)
# 5번답
y = s.split(" ")
print(y)

#6번답
s = "Python is a program language"
print(s[12:19])
#7번답
print(s[18:11:-1])
#8번답
print(s[20:28])

#9번답
colors = "magenta,red,blue,green,white,cyan,yellow"
c = colors.upper().split(",")
print(c)
#10번답
print(sorted(c))

