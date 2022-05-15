#矩陣的翻轉
#輸入
#2 3 (前面的2代表幾個陣列元素),最後是2維
#2是r 3是c?
#3 1 2
#8 5 4
#輸出
#3 8
#1 5
#2 4

#輸入一次
from sys import stdin #輸入
r, c = map(int, stdin.readline().split()) #讀取r 跟 c
arr = [] #宣告一個list
for y in range(r): #讀取 r列字串
    arr.append(stdin.readline().strip().split()) #添加元素到list裡
print(arr) #先列印看看 r是陣列數,c是每陣列裡的元素數
#輸入
# 2 3
# 3 1 2
# 8 5 4
#輸出
# [['3', '1', '2'], ['8', '5', '4']]
#for x in range(c): #依題意列印,字尾不換行
#    for y in range(r): 
#        print(arr[y][x], end=' ')
#    print() #印完一列才換行
'''
#輸入n次
from sys import stdin
for s in stdin:
    r, c = map(int, s.split())
    arr = []
    for y in range(r):
        arr.append(stdin.readline().strip().split())
#print(arr)
    for x in range(c):
        for y in range(r):
            print(arr[y][x], end=' ')
        print()
'''
'''
Python map（） 函數
Python 內置函數 Python 內置函數
描述
map（） 會根據提供的函數對指定序列做映射。
第一個參數 function 以參數序列中的每一個元素調用 function 函數，返回包含每次 function 函數返回值的新清單。
語法
map（） 函數語法：
map(function, iterable, ...)
參數
function -- 函數
iterable -- 一個或多個序列
返回值
Python 2.x 傳回清單。
Python 3.x 返回反覆運算器。
'''