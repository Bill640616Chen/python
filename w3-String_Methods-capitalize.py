#https://www.w3schools.com/python/ref_string_capitalize.asp
#Python -capitalize() Method
#Converts the first character to upper case
#轉換第一個字元為大寫
#Python 有一套內置的方法，您可以在字串上使用。
#注意：所有字串方法都會返回新的值。它們不會改變原始字串。
#Python 字串大寫（）方法
#案例本文中的第一個字母：
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x) #Hello, and welcome to my world.本句第一個字母改為大寫
#定義和使用
#The method returns a string where the first character is upper case, 
# and the rest is lower case.capitalize()
#這個方法返回字申的那裡第一個字元大寫,然後其他的是小寫
#語法
#string.capitalize()
#第一個字元轉換為大寫字元，其餘字元轉換為小寫字元：
txt = "python is FUN!"
x = txt.capitalize()
print (x) #Python is fun!
#如果第一個字元是數位，請查看會發生什麼：
txt = "36 is my age."
x = txt.capitalize()
print (x) #36 is my age.
print(txt.capitalize()) #36 is my age.
