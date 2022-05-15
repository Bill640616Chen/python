#https://www.w3schools.com/python/ref_string_strip.asp
#Python 字串 strip() Method
#Returns a trimmed version of the string
#返回字串的修剪版本
#Remove spaces at the beginning and at the end of the string:
#刪除字串開頭與結尾的空間：
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
#of all fruits banana is my favorite
#定義和使用
#The method removes any leading (spaces at the beginning) 
# and trailing (spaces at the end) characters (space is the default 
# leading character to remove)strip()
#該方法刪除任何引向（開頭的空間）和尾隨（末尾空格）字元
#（空間是預設的領導字元要刪除）
#Syntax語法
#string.strip(characters)
#Parameter Values參數值
#Parameter(參數)：Description(描述)
#characters(字元)：Optional(自選). A set of characters to remove as leading/trailing characters
#要刪除為領導/跟蹤字元的字元集
#Remove the leading and trailing characters:
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x) #banana
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.gt")
print(x) #rrttgg.....banana....rrr
#strip先從前面開始比對,再從後面比對,r前面有,,所以刪除,到後面r的後面沒參數可刪
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.rt")
print(x) #gg.....banana
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.rg")
print(x) #ttgg.....banana
#strip先從前面開始比對,再從後面比對