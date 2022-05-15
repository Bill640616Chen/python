
for i in input().split():
    n = eval(i) 
    print(["普通","吉","大吉"][(int(n)[0]*2+int(n)[1])%3])

#沒辦法執行
#https://zerojudge.tw/ShowThread?postid=28085&reply=0