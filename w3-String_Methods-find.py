#https://www.w3schools.com/python/ref_string_find.asp
#Python 字串 find() Method
#文本中的「歡迎」一詞在哪裡？：
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) #7 第7個位置
#定義和使用
#該方法首次發現指定值的發生。find()
#如果找不到值，則方法返回 -1。find()
#該方法與方法幾乎相同，唯一的區別是，如果找不到值，
#該方法會提出例外。（見下文範例）find()index()index()
#語法
#string.find(value, start, end)
#參數值
#Parameter(參數)：Description(描述)
#value(值)：Required(必填). The value to search for 尋找值
#start(開始)：Optional(自選). Where to start the search. Default is 0
#從哪裡開始,預設位置是0
#end(結束)：Optional(自選). Where to end the search. Default is to the end of the string
#在哪裡結束搜索,預設值是字串的末尾
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x) #1 位置1(最前的位置)
#當您僅在位置 5 和 10 之間搜索時，文字中字母「e」的第一次出現在哪裡？
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x) #8
txt = "Hello, welcome to my world."
x = txt.find("e", -12, -1)
print(x) 
#-1 ,就算是txt.find("e", -1, -12)也是-1,所以沒辦法用負數定義位置,當作找不到值
#如果找不到值，則查找（） 方法返回 -1，但索引（） 方法將提出一個例外：
txt = "Hello, welcome to my world."
print(txt.find("q")) #-1
print(txt.index("e")) #1
print(txt.index("q")) #ValueError: substring not found
