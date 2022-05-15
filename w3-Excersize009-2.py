def format(a):
    o = ord(a)-7
    return chr(o)
string = input()
ans = ""
for i in range(len(string)):
    ans += format(string[i])
print(ans)
#看不懂
#題目出處-解碼器
#https://zerojudge.tw/ShowProblem?problemid=a009
#輸入：1JKJ'pz'{ol'{yhklthyr'vm'{ol'Jvu{yvs'Kh{h'Jvywvyh{pvu5
#輸出：*CDC is the trademark of the Control Data Corporation.
#輸入：1PIT'pz'h'{yhklthyr'vm'{ol'Pu{lyuh{pvuhs'I|zpulzz'Thjopul'Jvywvyh{pvu5
#輸出：*IBM is a trademark of the International Business Machine Corporation.
'''
Python ord（） 函數
Python 內置函數 Python 內置函數

描述
ord（） 函數是 chr（） 函數（對於 8 位的 ASCII 字串）或 unichr（） 函數（對於 Unicode 物件）的配對函數，它以一個字元（長度為 1 的字元串）作為參數，返回對應的 ASCII 數值，或者 Unicode 數值，如果所給的 Unicode 字元超出了你的 Python 定義範圍，則會引發一個 TypeError 的異常。

語法
以下是 ord（） 方法的語法：

ord(c)
參數
c -- 字元。
返回值
返回值是對應的十進位整數。
'''
x = ord('a')
print(x)
x = ord('T')
print(x)
x="{} {}". format("hello",  "world")
print(x)
#不設置指定位置， 依預設順序'hello world'
x="{0} {1}". format("hello",  "world")
print(x)
# 設定指定位置'hello world'
x="{1} {0} {1}". format("hello",  "world")
print(x)
# 設定指定位置 'world hello world'