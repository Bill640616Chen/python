#https://www.w3schools.com/python/ref_string_isdigit.asp
#Python 字串 isdigit() Method
#檢查文字中的所有字元是否為數位：
txt = "50800"
x = txt.isdigit()
print(x) #True
#定義和使用
#如果所有字元都是數位，則方法返回 True，否則為錯誤。isdigit()
#指數，像2，也被認為是一個數位。
#語法
#string.isdigit()
#檢查文字中的所有字元是否為數位：
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ² (2次方的符號也算)
print(a.isdigit()) #True
print(b.isdigit()) #True