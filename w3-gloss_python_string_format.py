#https://www.w3schools.com/python/gloss_python_string_format.asp
#string_format 格式字串
#As we learned in the Python Variables chapter, we CANNOT combine strings and numbers like this:
#正如我們在 Python 變數章節中學到的，我們不能將字串和數字組合在一起：
'''
age = 36
txt = "My name is John, I am " + age
print(txt)
'''
#But we can combine strings and numbers by using the method!format()
#但是，我們可以使用這種方法將字串和數字結合起來！format()
#The method takes the passed arguments, formats them, and places them in the string where the placeholders are:format(){}
#該方法採用通過的參數，對它們進行格式化，並將它們放置在佔位元所在的字串中：format(){}
#Use the method to insert numbers into strings:format()
#使用該方法會插入字串：format()
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
print('-------------分隔線------------')
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
#格式（） 方法需要無限數量的參數，並放置到相應的佔位元元中：
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
print('-------------分隔線------------')
#You can use index numbers to be sure the arguments are placed in the correct placeholders:{0}
#您可以使用索引號確保參數被放置在正確的佔位元中：{0}
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#Related Pages 相關頁面
#Python Strings Tutorial Python 字串教程
#https://www.w3schools.com/python/python_strings.asp
#String Literals 字串文字
#https://www.w3schools.com/python/gloss_python_string_literals.asp
#Assigning a String to a Variable 將字串分配給變數
#https://www.w3schools.com/python/gloss_python_assign_string_variable.asp
#Multiline Strings 多行字串
#https://www.w3schools.com/python/gloss_python_strings_are_arrays.asp
#Strings are Arrays 字串是陣列
#https://www.w3schools.com/python/gloss_python_strings_are_arrays.asp
#Slicing a String 切片字串
#https://www.w3schools.com/python/gloss_python_string_slice.asp
#Negative Indexing on a String 字串上的負索引
#https://www.w3schools.com/python/gloss_python_string_negative_indexing.asp
#String Length 字串長度
#https://www.w3schools.com/python/gloss_python_string_length.asp
#Check In String 在字串裡檢查
#https://www.w3schools.com/python/gloss_python_check_string.asp
#Escape Characters 逃生字元
#https://www.w3schools.com/python/gloss_python_escape_characters.asp