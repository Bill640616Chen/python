#https://www.w3schools.com/python/ref_string_isspace.asp
#Python 字串 isspace() Method
#檢查文字中的所有字元是否為空白：
txt = "   "
x = txt.isspace()
print(x) #True
#定義和使用
#如果字串中的所有字元都是空白，則方法返回 True，否則為False。isspace()
#語法
#string.isspace()
#檢查文字中的所有字元是否為空白：
txt = "   s   "
x = txt.isspace()
print(x) #False