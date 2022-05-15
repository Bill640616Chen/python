#https://www.w3schools.com/python/ref_string_islower.asp
#Python 字串 islower() Method
#檢查文字中的所有字元是否都是小寫：
txt = "hello world!"
x = txt.islower()
print(x) #True
#定義和使用
#如果所有字元都是小寫，否則False，則方法返回True。islower()
#不檢查數位、符號和空間，只檢查字母字元。
#語法
#string.islower()
#檢查文字中的所有字元是否都是小寫：
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower()) #False
print(b.islower()) #True
print(c.islower()) #False