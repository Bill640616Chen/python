#矩陣的翻轉,無法執行

'''
score = [89, 55, 73, 66]
sum = 0
for i in range(4):
    sum = sum + score[i]
    print("第", i+1, "位同學成績為",score[i])
print(sum)

from sys import stdin
board = [[0]*100]*100
for s in board:
    row = s[0]     #列
    col = s[1]    #行
print(row) #測試row的值是元素還是陣列
print(col) #測試col的值是元素還是陣列
    for i in range(row):
        board[i] = input().split(' ')
        for j in range(col):
            board[i][j] = int(board[i][j])
    for i in range(col):
        for j in range(row):
            if(j == row - 1):
                print(int(board[j][i]))
            else:
                print(int(board[j][i]),end=' ')
'''

board = [[0]*2]*3
for s in board:
    row = s[0]     #列
    col = s[1]    #行
    for i in range(row):
        board[i] = input().split(' ')
        r = board[i]
    print(r)