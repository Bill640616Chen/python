#https://www.w3schools.com/python/ref_string_isupper.asp
#Python 字串 isupper() Method
#檢查文字中的所有字元是否大寫：
txt = "THIS IS NOW!"
x = txt.isupper()
print(x) #True
#定義和使用
#如果所有字元都大寫，則方法返回True，否則為False。isupper()
#不檢查數位、符號和空間，只檢查字母字元。
#語法
#string.isupper()
#檢查文字中的所有字元是否大寫：
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"
d = "ABC-12.3/?"
print(a.isupper()) #False
print(b.isupper()) #False
print(c.isupper()) #True
print(d.isupper()) #True