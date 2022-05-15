#https://www.w3schools.com/python/ref_string_partition.asp
#Python 字串 partition() Method
#搜索「香蕉」一詞，並返回帶有三個元素的元組tuple：
#1-everything before the "match"
#2-the "match"
#3-everything after the "match"
txt = "I could eat bananas all day"
x = txt.partition("bananas") #partition分區,用bananas match後分區
print(x) 
#('I could eat ', 'bananas', ' all day')->元組tuple(裡面有三個元素)
#定義和使用
#The method searches for a specified string, and splits the string 
#into a tuple containing three elements.partition()
#這方法搜尋一個指定的字申,拆分這個字申到一個元組tuple陣列要包含三個元素
#The first element contains the part before the specified string.
#第一個元素要含這部分要在指定字申之前
#The second element contains the specified string.
#第二個元素要含指定的字串
#The third element contains the part after the specified string.
#第三個元素要含這部分要在指定字申之後
#Note: This method search for the first occurrence of the specified string.
#筆記：此方法搜索指定字串的首次出現。
#Syntax語法
#string.partition(value)
#Parameter Values 參數值
#Parameter(參數)：Description(描述)
#value(值)：Required(必填). The string to search for 用來分區字串的值
#If the specified value is not found, the partition() method returns 
# a tuple containing: 1 - the whole string, 2 - an empty string, 
# 3 - an empty string:
#如果指定的值沒有發現,partition的方法會一個元組陣列裡含有
# 1.全部的字申,2.空的字申,3.空的字申,123代表3個元素
#所以第一個元素是全部的字申,第二個元是空的字申,因為字申裡沒有那個值,
#第三個元素就排在第三個空字申
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x) #('I could eat bananas all day', '', '')
#字串裡沒有apples,所以第2,3元素都是空的