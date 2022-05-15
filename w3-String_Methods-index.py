#https://www.w3schools.com/python/ref_string_index.asp
#Python 字串 index() Method
#文本中的「歡迎」一詞在哪裡？：
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x) #7,索引的值在那個位置出現
#定義和使用
#該方法首次發現指定值的發生。index()
#如果找不到值，則該方法會提出例外。index()
#該方法幾乎與方法相同，唯一的區別是，如果找不到值，該方法將返回 -1。（見下文範例）index()find()find()
#語法
#string.index(value, start, end)
#參數值
#Parameter(參數)：Description(描述)
#value(值)：Required(必填). The value to search for
#start(起始)：Optional(自選). Where to start the search. Default is 0
#end(結束)：Optional(自選). Where to end the search. Default is to the end of the string
#文本中字母「e」的第一次出現在哪裡？：
txt = "Hello, welcome to my world."
x = txt.index("e")
print(x) #1,索引的值在那個位置出現
#當您僅在位置 5 和 10 之間搜索時，文字中字母「e」的第一次出現在哪裡？
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x) #8,在索引位置5跟位置10找,出現在位置8
#如果找不到值，則查找（） 方法返回 -1，但索引（） 方法將提出一個例外：
txt = "Hello, welcome to my world."
print(txt.find("q")) #find找不到,返回值-1
print(txt.index("q")) 
#index找不到,ValueError: sub-string not found,值錯誤:子字申找不到
