#https://www.w3schools.com/python/ref_string_startswith.asp
#Python 字串 startswith() Method
#Returns true if the string starts with the specified value
#如果字串從指定值開始，則傳回True
#Check if the string starts with "Hello":
#檢查字串是否以「Hello」開頭：
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x) #True
#定義和使用
#如果字串以指定值開頭，則方法返回 True，否則False。startswith()
#Syntax語法
#string.startswith(value, start, end)
#Parameter Values參數值
#Parameter(參數)：Description(描述)
#value(值)：Required(必填). The value to check if the string starts with
#檢查字串是否以值開始
#start(開始)：Optional(自選). An Integer specifying at which position to start the search
#指定開始搜尋的位置
#end(結束)：Optional(自選). An Integer specifying at which position to end the search
#指定結束搜尋的位置
#Check if position 7 to 20 starts with the characters "wel":
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x) #True
