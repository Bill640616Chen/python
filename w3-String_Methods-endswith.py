#https://www.w3schools.com/python/ref_string_endswith.asp
#Python 字串 endswith() Method
#檢查字串是否以標點符號結尾 （.）：
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x) #True
#定義和使用
#如果字串以指定值結束，否則錯誤，則方法返回 True。endswith()
print(txt.endswith(".")) #True
#語法
#string.endswith(value, start, end)
#string.endswith(value, start)
#參數值
#Parameter(參數)：Description(描述)
#value(值)：Required(必填)，The value to check if the string ends with
#這值去檢查字申最後是否有
#start(開始)：Optional(自選)，An Integer specifying at which position to start the search
#一個數字指定開始搜索的位置
#end(結束)：Optional(自選)，An Integer specifying at which position to end the search
#一個數字指定結束搜索的位置
#檢查字串是否以短語「我的世界」結尾。
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x) #True
#檢查位置 5 到 11 是否以短語「我的世界」結尾。
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11) #18,27為True,因為26不是含.
print(x) #False

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", -13, -1) #不支援負數做始末位置的值,所有都False
print(x) #False
txt = "Hello, welcome to my world."
x = txt.endswith("my world.",-10) #位置-9為m是可以的,-10也可以
print(x) #True
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 18,27) #18,27為True,因為26不含.
print(x) #True