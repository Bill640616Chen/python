#https://zerojudge.tw/ShowProblem?problemid=a010
from sys import stdin
#stdin 用於所有互動式輸入（包括對input（）的調用）
def gp(n,k):
    c =0
    while (n % k ==0):
        c += 1
        n //= k
        #取整除賦值運算子
    return n,c
    #回傳n可以連除幾次k,還有除完還剩的n值
def fmt(x, y): #x的y次方
    if y==1 : return str (x)
    return '{}^{}'.format(x,y)
#這裡預備一個函數來處理輸出
for s in stdin: #連續輸入
    n = int(s)  #轉為整數
    m = int(n**0.5) + 1 
    #檢測的上限,n**0.5就是n的平方根,質數只要檢測到平方根即可
    #int()傳回一個整個,無條年捨去
    r = []      #先不管輸出,把結果先存起來
    n, c = gp(n, 2) #把2代入k,當作是最小除數
    if c : r.append(fmt(2,c))
    #if c : c為int,c>0就為true,c=0為None
    #如果c>0,就會存到r裡
    for i in range(3,m,2): #range(start,end,step)
    #從3檢測到m,只檢測奇數
        if i > n : break
    #檢測過程,發現n比i小就中斷
        n, c = gp(n, i)
    #開始檢測i值
        if c : r.append(fmt(i,c))
    #如果回傳值c > 0, 表示i是n的質因數
    #把i及次數c記錄下來
    if n > 1 : r.append(fmt(n,1))
    #跑完迴圈之後,如果n > 1,肯定剩下的n是質數
    #把n及次數1記錄下來
    print(r)
    print('*'.join(r))
    break
    #join可以把字串,串起來輸出
