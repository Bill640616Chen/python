#https://www.w3schools.com/python/ref_string_istitle.asp
#Python 字串 istitle() Method
#檢查每個單字是否以大寫字母開頭：
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x) #True
#定義和使用
#如果文本中的所有單詞都以上個案字母開頭，並且其餘單詞是小寫字母，
# 否則False，則方法返回 True。istitle()
#符號和數位被忽略。
#語法
#string.istitle()
#檢查每個單字是否以大寫字母開頭：
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle()) #False
print(b.istitle()) #True
print(c.istitle()) #True
print(d.istitle()) #True