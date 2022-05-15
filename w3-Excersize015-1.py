#矩陣的翻轉
'''
from sys import stdin
board = [[0]*100]*100
for s in stdin:
    t = s.split(' ')
    row = t[0]     #列
    #輸入23333,輸出也是23333,因為輸出清單只有一個項目
    #col = int(t[1])     #行
    break
print(t)
print(row)

from sys import stdin
row = t[0]
board = [[0]*100]*100
for i in range(row):
    board[i] = input().split(' ')
    for j in range(col):
        board[i][j] = int(board[i][j])
        break
'''
#from sys import stdin
#for s in stdin:
#    t = s.split(' ')
#print(t)
#輸入233333
#輸出['233333\n'],因為split(' ')裡面的空白,變成\n換行符號
#x = input().split()
#輸入23333
#print(x)
#輸出['23333']清單
'''
from sys import stdin
#board = [[0]*100]*100
#1個list裡有100個0,*100代表有100個list,1維變2維
for s in stdin:
    #t = int(s)
    row = s[0][1][2]    #列
    #col = s[1]     #行
    break
print(row)
#print(col)
'''
print('---------陣列維數寫法---------')
a = [[1]*2]*3
b = [[2]*2]*5
print(a)
#[[1, 1], [1, 1], [1, 1]]
s = [a]*3 #變三維
print(s[0][1][1])
#[[[1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1]]]

#for i in range(col):
#    for j in range(row):
#        if(j == row - 1):
#                print(int(board[j][i]))
#            else:
#                print(int(board[j][i]),end=' ')
