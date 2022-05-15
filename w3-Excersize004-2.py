
try:
    while True:
        y=int(input())
        if y%400!=0 and y%4!=0:
            print('平年')
        else :
            print('閏年') 
            break
        raise Exception('EOF')
except Exception as e:
     print(e)



#f=open(r"c:\Users\user\DownLoads\member.txt)
#c:前面加r,是讓程式認為後面是個路徑,不然會出錯,要不單個\換成\\

from sys import stdin
for i in map(int,stdin):
    print((lambda y:"閏年" if ((y%4==0) and (y%100!=0)) or (y%400==0) else "平年")(i))
    break