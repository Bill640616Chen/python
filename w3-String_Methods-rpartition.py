#https://www.w3schools.com/python/ref_string_rpartition.asp
#Python 字串 rpartition() Method
#搜索「香蕉」一詞的最後一次出現，並返回帶有三個元素的元組tuple：
#1-everything before the "match"
#2-the "match"
#3-everything after the "match"
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
#定義和使用
#The method searches for the last occurrence of a specified string, 
#and splits the string into a tuple containing three elements.rpartition()
#這方法搜尋一個指定的字申的最後一組字元,拆分這個字申到一個元組tuple陣列要包含三個元素
#The first element contains the part before the specified string.
#第一個元素要含這部分要在指定字申之前
#The second element contains the specified string.
#第二個元素要含指定的字串
#The third element contains the part after the specified string.
#第三個元素要含這部分要在指定字申之後
#語法
#string.rpartition(value)
#參數值
#Parameter(參數)：Description(描述)
#value(值)：Required(必填). The string to search for
#If the specified value is not found, the rpartition() method returns
#a tuple containing:1.an empty string, 2.an empty string, 3.the whole string:
#如果未找到指定值，則 rpartition() 方法傳回包含的tuple：1.空字串，2.空字串，3.整個字串：
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)
#('', '', 'I could eat bananas all day, bananas are my favorite fruit')