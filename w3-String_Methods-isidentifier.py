#https://www.w3schools.com/python/ref_string_isidentifier.asp
#Python 字串 isidentifier() Method
#檢查字串是否為有效識別碼：
txt = "Demo"
x = txt.isidentifier()
print(x) #True
#定義和使用
#如果字串是有效的標識符，否則該方法返回 True。isidentifier()
#如果字串僅包含字母數位字母 （a-z） 和 （0-9）， 或下劃線 （_）
# ，則該字串被視為有效的識別符。有效的標識碼不能從數字開始，也不能包含任何空格。
#語法
#string.isidentifier()
#檢查字串是否為有效識別碼：
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier()) #True
print(b.isidentifier()) #True
print(c.isidentifier()) #False
print(d.isidentifier()) #False