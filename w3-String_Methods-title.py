#https://www.w3schools.com/python/ref_string_title.asp
#Python 字串 title() Method
#Converts the first character of each word to upper case
#轉換每個字的第一個字元為大寫
#Make the first letter in each word upper case:
txt = "Welcome to my world"
x = txt.title()
print(x) #Welcome To My World
#定義和使用
#The method returns a string where the first character in every word is upper case. Like a header, or a title.title()
#這個方法傳回一個字串的內容為每個字的第一個字元都是大寫
#If the word contains a number or a symbol, the first letter after that will be converted to upper case.
#如果字包含一個數字或一個符號,第一個字母在數字或符號後面將會轉換為大寫
#Syntax語法
#string.title()
#Parameter Values參數值
#No parameters.無參數
#Make the first letter in each word upper case:
txt = "Welcome to my 2nd world"
x = txt.title()
print(x) #Welcome To My 2Nd World
#Note that the first letter after a non-alphabet letter is converted into a upper case letter:
#請注意,第一個字母在非字母後面一樣轉換為大寫
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x) #Hello B2B2B2 And 3G3G3G