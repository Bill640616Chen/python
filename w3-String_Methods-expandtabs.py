#https://www.w3schools.com/python/ref_string_expandtabs.asp
#Python 字串 expandtabs() Method
#將選項卡大小設定為 2 個空白：
txt = "H\te\tl\tl\to" #\t tab鍵的空格功能
x =  txt.expandtabs(2) #2,只有一個空白
#expandtabs的參數是指定位點之間要隔幾個字元,以第一個例子來說,定位點之間隔兩個字元
#第一個被接著的字母佔去,所以只剩第二個位置是空白
print(x) #H e l l o
txt = "H\te\tl\tl\to"
print(txt) 
#H       e       l       l       o,\t預設是8格空白,然後第一格被佔住,所以隔7格
txt = '1\t12\t123\t1234\t12345\t123456'
print(txt) #1       12      123     1234    12345   123456
#            7格      6格       5格      4格      3格
#\t預設是8格空白,依序看下一組多少字元,用8去減=要空的格數
#語法
#string.expandtabs(tabsize)
#參數值
#Parameter(參數)：Description(描述)
#tabsize(tab大小)：Optional(自選). 
#指定=tab大小的數。預設tab大小為8,第11,15行就有解釋
#使用不同的選項卡大小檢視結果：
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs()) #沒填數字,就是使用預設
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
#H       e       l       l       o 字元間空格數8-1=7
#H       e       l       l       o 字元間空格數8-1=7
#H e l l o 字元間空格數2-1=1
#H   e   l   l   o 字元間空格數4-1=3
#H         e         l         l         o 字元間空格數10-1=9