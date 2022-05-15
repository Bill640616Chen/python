#https://www.w3schools.com/python/ref_string_isdecimal.asp
#Python 字串 isdecimal() Method
#檢查單碼物件中的所有字元是否為小數：
txt = "\u0033" #unicode for 3
x = txt.isdecimal() #decimal是小數
print(x) #True
#定義和使用
#如果所有字元都是小數（0-9），則方法返回正確。isdecimal()
#此方法用於單碼物件。
#語法
#string.isdecimal()
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal()) #True
print(b.isdecimal()) #False