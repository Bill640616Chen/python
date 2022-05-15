#https://www.w3schools.com/python/ref_string_rstrip.asp
#Python 字串 rstrip() Method
#Returns a right trim version of the string
#返回字串的右修剪版本
#Remove any white spaces at the end of the string:
#在字串最後面移除任何空白
txt = "     banana     "
x = txt.rstrip() #沒字元,預設是空白
print("of all fruits", x, "is my favorite")
#of all fruits      banana is my favorite
#定義和使用
#The method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.rstrip()
#該方法刪除任何尾隨字元(字元在字申的後面),空白是預設的尾隨字元to remove.　rstrip()
#Syntax語法
#string.rstrip(characters)
#Parameter Values參數值
#Parameter(參數)：Description(描述)
#characters(字元)：Optional(自選). 
#A set of characters to remove as trailing characters
#要刪除為尾隨字元的一組字元
#從字尾開始刪除指定的字元(實作後的了解)
#如果尾隨字元是逗號(標準符號)、s、q 或 w，請刪除：
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x) #banana
txt = "banana,,,,,ssqqqww.....眼鏡"
x = txt.rstrip(",.qsw")
print(x) #banana,,,,,ssqqqww.....眼鏡
#從字尾開始刪除指定的字元
txt = "banana,,,,,ssqqqww.....glass"
x = txt.rstrip(",.qsw")
print(x) #banana,,,,,ssqqqww.....gla
#從字尾開始刪除指定的字元