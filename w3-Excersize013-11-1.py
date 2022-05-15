#range()的了解
#n = '1I5V10X50L100C500D1000M'
#print(len(n))
#for i in range(len(n)-2,-2,-2):
   #長度可以-2,但是後面兩個參數的作用,造成無法遍歷
    #print裡要有[i]才會有長度-2的輸出
    #若沒有[i]遍歷,則print(n)則印出完整的長度
    #print(n[i]) #有break,只會傳回1個值
    #for i in range(len(n))
    #23-2=21,所以索引輸出是'1I5V10X50L100C500D100'
    #range(len(n)-2,-2,-2),00D0C0L50VIM
    #從索引21位置0開始,往前2個遍歷
    #然後到索引-2位置(就是到最前面後,再回到最後面數到-2)
    #原始字串是'1I5V10X50L100C500D1000M'
    #print(len(n))
    #print(n) #1I5V10X50L100C500D1000M
    #沒有break,則遍歴23(字串的長度)次字串,有break遍歷1次
    #break
#a=list(range(21,-2,-2))
#print(a)
#[21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1]
#n = '1I5V10X50L100C500D1000M'
#for i in range(-2,-24,-2):
#    print((n[i]))
#00D0C0L50VI
#想把遍歷的輸出變成以清單顯示,沒成功
n = '1I5V10X50L100C500D1000M'
a = []
for i in range(-2,-24,-2):
    r = n[-1]
    a.append(r)
print(a) #11個M

score=[90]*10 #list index range,50為list裡的元素個數
print(score)
sum=0
for i in range(10):
    sum = sum + score[i] #90加了50次
print(sum)
b = [[0]*2]*6
print(b)
#[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

score = [89, 55, 73, 66]
sum = 0
for i in range(4):
    sum = sum + score[i]
    print("第", i+1, "位同學成績為",score[i])
print(sum)

#費氏數列
fib = [0]*100
fib[0] = 1
fib[1] = 1
for i in range(2,100):
    fib[i] = fib[i-1] + fib[i-2]
for i in range(100):
    print(i+1, fib[i])

score=[[0]*5 for i in range(5)]
#[0]*5內圈,range(5)外圈
print(score)
#二維陣列,5個1維,1維裡有5個0

for i in range(5): #遍歷5次,外圈2維
    for j in range(4): #遍歷4次,內圈1維
        score[i][j]=2 
print(score)
#從i=0開始進到內圈索引[0][0].[0][1].[0][2],都是2
#i=1開始進到內圈索引[1][0],[1][1],[1][2],也是2
#i=2開始進到內圈索引[2][0],[2][1],[2][2],也是2
#因為range(3),是遍歷3次
'''
#陣列初始化（一）個別初始化
A=[2]*5 #[0],這裡的[]代表清單,5是清單的元素個數
A[0] = 89 #索引位置0是89
A[1] = 55
A[2] = 73
A[3] = 66
#陣列初始化（二）串列初始化
print(A)
#[89, 55, 73, 66, 0]
#陣列初始化（三）迴圈初始化
A=[0]*4
for i in range(4):
    A[i]=90
print(A)
#[90, 90, 90, 90]
'''
#score = [10]*5
#[10, 10, 10, 10, 10]
#score=[[0]*40 for i in range(5)]
#每個一維陣列有40個0,有五個陣列
#print(score)

#range(10),10不算在內
#print(n[-1]) #M
#n1 = '123456'
#list2 = ['M','A','C']
#list1 = list(n1)
#list2.extend(list1)
#print(list2)
#['M', 'A', 'C', '1', '2', '3', '4', '5', '6']