#https://www.w3schools.com/python/ref_string_rfind.asp
#Python 字串 rfind() Method
#Searches the string for a specified value and returns the last position of where it was found
#搜索字串以尋找指定值，並傳回哪裡找到的最後位置
#文字中字串「casa」的最後一次出現在哪裡？：
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x) #12在位置第12找到
print(txt.index("casa",10,20))
#12,如果要有相同結果,則必須有索引區間
#定義和使用
#該方法發現指定值的最後發現位置。rfind()
#如果找不到值，則方法返回 -1。rfind()
#該方法幾乎與該方法相同。請參閱下面的範例。rfind()rindex()
#Syntax語法
#string.rfind(value, start, end)
#參數值
#Parameter(參數)：Description(描述)
#value(值)：Required(必填). The value to search for
#start(值)：Optional(自選). Where to start the search. Default is 0
#end(值)：Optional(自選). Where to end the search. Default is to the end of the string
#字母「e」的最後一次出現在文本中的位置？
txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x) #13
#當您僅在位置 5 和 10 之間搜索時，文字中字母「e」的最後出現位置在哪裡？
txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)
print(x) #8
#rfind是找最後位置的值,也可以區間搜索
#index是找最前面的位置的值,也可以區間搜索
#如果未找到值，rfind（） 方法返回 -1，但 rindex（） 方法將提出例外：
txt = "Hello, welcome to my world."
print(txt.rfind("q")) #-1
print(txt.rindex("q")) #substring not found