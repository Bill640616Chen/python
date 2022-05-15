#https://www.w3schools.com/python/ref_string_isnumeric.asp
#Python 字串 isnumeric() Method
#檢查文字中的所有字元是否都是數位字元：
txt = "565543"
x = txt.isnumeric()
print(x) #True
#如果所有字元都是數位 （0-9）， 否則錯誤，則方法返回 True。isnumeric()
#指數，如 2 和 3/4 也被視為數位值。
#"-1"並且不被視為數位值，因為字串中的所有字元必須是數位值，並且不是數位值。"1.5"-
#語法
#string.isnumeric()
#檢查字元是否為數位：
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ² (2次方的符號也算)
c = "10km2"
d = "-1"
e = "1.5"
print(a.isnumeric()) #True
print(b.isnumeric()) #True
print(c.isnumeric()) #False,英文非數字
print(d.isnumeric()) #False,有負號不行
print(e.isnumeric()) #False,小數點也不行