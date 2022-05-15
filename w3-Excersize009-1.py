n = input()
def password():
    m = ""
    for i in n:
        m = int(ord(i)) - 7
        #透過ord把字母或符號轉為數字代入chr裡,輸出一個字母
        #ord('str')字母或符號轉為數字,chr('int')數字轉為字母
        print(chr(m),end = '')
password()
#看不懂
#題目出處-解碼器
#https://zerojudge.tw/ShowProblem?problemid=a009
#用來了解上面的步驟
print('\n')
print(ord('J'))
print(chr(67))
'''
Python ord()函數
Python 內置函數 Python 內置函數

描述
ord()函數是 chr()函數（對於 8 位的 ASCII 字串）或 unichr()函數
（對於 Unicode 物件）的配對函數，它以一個字元（長度為 1 的字元串）作為參數，
返回對應的 ASCII 數值，或者 Unicode 數值，如果所給的 Unicode 字元
超出了你的 Python 定義範圍，則會引發一個 TypeError 的異常。

語法
以下是 ord()方法的語法：

ord(c)
參數
c -- 字元。
返回值
返回值是對應的十進位整數。
print(ord('a'))
97

--------------------------------------------------------------
Python chr()函數
Python 內置函數 Python 內置函數
描述
chr()用一個範圍在 range（256）內的（就是0~255）整數作參數，返回一個對應的字元。
語法
以下是 chr()方法的語法：
chr(i)
參數
i -- 可以是10進位也可以是16進位的形式的數位。
返回值
返回值是當前整數對應的 ASCII 字元。
實例
以下展示了使用 chr()方法的實例：
print chr（0x30）， chr（0x31）， chr（0x61） # 十六進位
0 1 a
print chr（48）， chr（49）， chr（97） # 十進位
0 1 a
'''
