#羅馬數字的規則,往前是減,往後是加
#dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
str = '1I5V10X50L100C500D1000M'
#[0]1[1]I[2]5[3]V[4:6]10[6]X[7:9]50[9]L[10:13]100[13]C[14:17]500[17]D
#[18:22]1000[22]M
#r =""
#print(str[1]*3)
n = int(input())
if n == 1000:
    print(str[22])
#100
elif n == 9:
    print(str[1]+str[6])
elif n -1 ==2 or n-1 ==1:
    print(str[1]*3)
    print(str[1]*2)




x,y,z = input() 
print(int(x),int(y),int(z))
#x,y,z只能一個位數
#例:輸入233,輸出2 3 3
x,y = input().split()
print(x,y)
#左邊二個變數以上,右邊使用split()時,則輸入時,只能各一個位數,並且要空白隔開
#例:輸入2 3,輸出2 3
x,y = input().split(' ')
print(x,y)
#左邊二個變數以上,右邊使用split(' ')時,則輸入時,
#兩個變數沒限位數長度,但中間要空白隔開
#例:輸入222 33333,輸出222 33333

'''
from sys import stdin
for s in stdin: 
    if int(s) % 3 == 0 and 1 < int(s) < 5:
        n = int(s) // 2
    #if int(s) == 12:
        r = dict.get(int(n))
    print(type(s))
    print(r+r+r)
    break
'''
#n = dict.get(1)
#print(n+n+n)
#list1 = list(dict)
#print(list1) #印出鍵