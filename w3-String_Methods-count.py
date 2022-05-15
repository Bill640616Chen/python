#https://www.w3schools.com/python/ref_string_count.asp
#Python 字串 count() Method
#傳回字串中顯示值「蘋果」的次數：
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x) #2
#因為計算是int,所以寫成print = txt.int(count("apple"))是無法輸出的
print(txt.count('apple')) #2
#count('apple')本身就是int,所以不用print(int(txt.count('apple'))) #2這樣寫
#定義和使用
#該方法返回字串中指定值顯示的次數。count()
#語法
#string.count(value, start, end)
#參數值
#Parameter(參數)：Description(描述)
#value(值)：Required(必填)， A String. The string to value to search for
#start(開始)：Optional(自選)， An Integer. The position to start the search.
# Default is 0
#end(結束)：Optional(自選)， An Integer. The position to end the search.
# Default is the end of the string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x) #1
print(txt.count("apple", 10, 24)) #1